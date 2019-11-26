from selenium.webdriver.common.by import By


class CopperSearchResults:
    search_result_first_item = (By.CSS_SELECTOR, ".search-article-api-content li:nth-child(1) h3 a")

    def __init__(self, browser):
        self.browser = browser

    def get_first_match(self):
        search_results = self.browser.find_element(*self.search_result_first_item)
        return search_results.get_attribute('textContent')
