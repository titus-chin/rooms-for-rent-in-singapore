from collections import defaultdict
import pandas as pd
import scrapy
from scrapy.crawler import CrawlerProcess
from src.data.utils import get_project_root, load_config
from src.data.preprocessing import check_urls, get_contents, get_next_page


def main(base_url, country_code, areas, min_rent, max_rent, output_path):
    """Pipeline to scrape rental lists from roomz.asia. Append contents
    of valid rental lists to a dictionary, then write the data to a csv
    file.

    Parameters
    ----------
    base_url : str
        Base url of roomz.asia.
    country_code : str
        Country code used in roomz.asia url, either sg or my.
    areas : iterable
        Areas to scrape, will be used in roomz.asia url.
    min_rent : int or float
        Minimum rent to scrape.
    max_rent : int or float
        Maximum rent to scrape.
    output_path : str
        Path to output file.
    """
    rental_dict = defaultdict(list)

    class Rental_Spider(scrapy.Spider):
        """Spider that crawls over multiple websites to scrape rental
        lists.
        """

        name = "rental_spider"
        start_urls = {base_url.format(country_code, area) for area in areas}

        def parse(self, response):
            """Check the contents of each url. If it is a valid url,
            append the contents to a dictionary. Repeat the same for
            the following pages until it encounters an invalid url.
            """
            content = response.json()
            if check_urls(content) == "valid_urls":
                get_contents(content, rental_dict, country_code, min_rent, max_rent)
                next_page = get_next_page(response.url)
                yield scrapy.Request(url=next_page)

    process = CrawlerProcess()
    process.crawl(Rental_Spider)
    process.start()

    rental_df = pd.DataFrame(rental_dict)
    rental_df.to_csv(output_path, index=False)


if __name__ == "__main__":
    conf = load_config("conf", "parameters", "data.yaml")
    output_path = get_project_root().joinpath("data", conf["output_file"])
    main(
        base_url=conf["base_url"],
        country_code=conf["country_code"],
        areas=conf["areas"],
        min_rent=conf["min_rent"],
        max_rent=conf["max_rent"],
        output_path=output_path,
    )
