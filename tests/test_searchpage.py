import pytest
from selenium import webdriver
from pages.search import CopperSearchPage
from pages.results import CopperSearchResults


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_search_phrase(browser):
    copper_searchpage = CopperSearchPage(browser)
    copper_searchpage.load()
    copper_searchpage.search_item("developer")

    copper_resultspage = CopperSearchResults(browser)
    assert copper_resultspage.get_first_match() == "Join the Developer Forum"
