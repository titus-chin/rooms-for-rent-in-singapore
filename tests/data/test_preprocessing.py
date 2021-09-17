from src.data.preprocessing import check_urls, get_contents, get_next_page
import pytest
import requests
from collections import defaultdict


@pytest.fixture
def valid_rental_url():
    url = "https://sg.roomz.asia/api?c=Rooms&a=getAsyncDataForListPage&area=east-singapore&rentalType=3&page=1"
    response = requests.get(url)
    return response.json()


@pytest.fixture
def invalid_rental_url():
    url = "https://sg.roomz.asia/api?c=Rooms&a=getAsyncDataForListPage&area=east-singapore&rentalType=3&page=1000"
    response = requests.get(url)
    return response.json()


class TestCheckUrls:
    def test_on_valid_rental_url(self, valid_rental_url):
        content = valid_rental_url
        assert check_urls(content) == "valid_urls"
        assert isinstance(check_urls(content), str)

    def test_on_invalid_rental_url(self, invalid_rental_url):
        content = invalid_rental_url
        assert check_urls(content) is None


class TestGetContents:
    def test_on_valid_rental_url(self, valid_rental_url):
        content = valid_rental_url
        rental_dict = defaultdict(list)
        if check_urls(content) == "valid_urls":
            get_contents(
                content=content,
                dict=rental_dict,
                country_code="sg",
                min_rent=200,
                max_rent=1500,
            )
        assert [*rental_dict.keys()] == [
            "Area",
            "Location",
            "Rent (S$/month)",
            "Headline",
            "Link",
        ]
        assert len(rental_dict) >= 1

    def test_on_invalid_rental_url(self, invalid_rental_url):
        content = invalid_rental_url
        rental_dict = defaultdict(list)
        if check_urls(content) == "valid_urls":
            get_contents(
                content=content,
                dict=rental_dict,
                country_code="sg",
                min_rent=200,
                max_rent=1500,
            )
        assert [*rental_dict.keys()] == []
        assert len(rental_dict) == 0


class TestGetNextPage:
    def test_on_page_1(self):
        current_page = "https://sg.roomz.asia/api?c=Rooms&a=getAsyncDataForListPage&area=east-singapore&rentalType=3&page=1"
        next_page = "https://sg.roomz.asia/api?c=Rooms&a=getAsyncDataForListPage&area=east-singapore&rentalType=3&page=2"
        assert get_next_page(current_page) == next_page
        assert isinstance(get_next_page(current_page), str)

    def test_on_page_99(self):
        current_page = "https://sg.roomz.asia/api?c=Rooms&a=getAsyncDataForListPage&area=east-singapore&rentalType=3&page=99"
        next_page = "https://sg.roomz.asia/api?c=Rooms&a=getAsyncDataForListPage&area=east-singapore&rentalType=3&page=100"
        assert get_next_page(current_page) == next_page
        assert isinstance(get_next_page(current_page), str)
