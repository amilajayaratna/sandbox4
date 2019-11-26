from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CopperSearchPage:
    URL = "https://support.copper.com/hc/en-us"
    search_box = (By.CSS_SELECTOR, ".title-block #query")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search_item(self, phrase):
        search_inputbox = self.browser.find_element(*self.search_box)
        search_inputbox.send_keys(phrase)
        search_inputbox.send_keys(Keys.RETURN)
