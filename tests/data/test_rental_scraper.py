from src.data.rental_scraper import main
import pandas as pd
import os


class TestMain:
    def test_on_main_pipeline(self):
        base_url = "https://{}.roomz.asia/api?c=Rooms&a=getAsyncDataForListPage&area={}&rentalType=3&page=1"
        country_code = "sg"
        areas = ["east-singapore"]
        min_rent = 200
        max_rent = 1500
        output_file = "test_singapore_rental_lists.csv"
        main(base_url, country_code, areas, min_rent, max_rent, output_file)
        test_df = pd.read_csv(output_file)
        try:
            assert test_df.shape[0] >= 1
            assert test_df.shape[1] == 5
            assert isinstance(test_df, pd.DataFrame)
        finally:
            os.remove(output_file)
