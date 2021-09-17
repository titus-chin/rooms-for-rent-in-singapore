from datetime import date
import re


def check_urls(content):
    """If an url contains rental lists and the first list is updated at
    either this year or last year, it is a valid url.

    Parameters
    ----------
    content : dict
        Json data obtained from the urls.

    Returns
    -------
    str or NoneType
    """
    if content["data"]["lists"] is not None:
        last_year = date.today().year - 1
        if int(content["data"]["lists"][0]["update_time"][:4]) >= last_year:
            return "valid_urls"


def get_contents(content, dict, country_code, min_rent, max_rent):
    """Check if the rental list is updated and affordable. Append area,
    location, rent, headline and link of valid lists to a dictionary.

    Parameters
    ----------
    content : dict
        Json data obtained from the urls.
    dict : collections.defaultdict
        Dictionary that stores all the scraped contents.
    country_code : str
        Country code used in roomz.asia url, either sg or my.
    min_rent : int or float
        Minimum rent to scrape.
    max_rent : int or float
        Maximum rent to scrape.
    """
    last_year = date.today().year - 1
    for list in content["data"]["lists"]:
        rent = int(list["rent"].replace(",", ""))
        condition_1 = int(list["update_time"][:4]) >= last_year
        condition_2 = min_rent <= rent <= max_rent
        if condition_1 & condition_2:
            dict["Area"].append(content["data"]["area"])
            dict["Location"].append(list["location_name"])
            dict[f"Rent ({'RM' if country_code == 'my' else 'S$'}/month)"].append(rent)
            dict["Headline"].append(list["headline"])
            dict["Link"].append(f"https://{country_code}.roomz.asia/{list['id']}")


def get_next_page(current_page):
    """Return next page based on current page url.

    Parameters
    ----------
    current_page : str
        Current page url.

    Returns
    -------
    str
    """
    regex = r"(?<=page=)\d+"
    next_page_number = str(int(*re.findall(regex, current_page)) + 1)
    return re.sub(regex, next_page_number, current_page)
