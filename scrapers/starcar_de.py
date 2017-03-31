import platform
from selenium import webdriver
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from contextlib import contextmanager


phantomjs_path = ""
driver = ""

try:
    if platform.system() == "Linux":
        if platform.machine() == "x86_64":
            phantomjs_path="./drivers/phantomjs/linux/x86_64/bin/phantomjs"
        else:
            phantomjs_path="./drivers/phantomjs/linux/i686/bin/phantomjs"
finally:
    driver = webdriver.PhantomJS(phantomjs_path)


country_combo_selector = '#country'
place_combo_xpath = '//*[@id="pickup"]'


class Crawler:

    def __init__(self):
        try:
            if platform.system() == "Linux":
                if platform.machine() == "x86_64":
                    phantomjs_path = "./drivers/phantomjs/linux/x86_64/bin/phantomjs"
                else:
                    phantomjs_path = "./drivers/phantomjs/linux/i686/bin/phantomjs"
        finally:
            self.browser = webdriver.PhantomJS(phantomjs_path)
            self.browser.get("https://www.starcar.de/stationen")

    @contextmanager
    def wait_for_page_load(self, element ,timeout=30):
        yield
        WebDriverWait(self.browser, timeout).until(staleness_of(element))

    def look_up(self):
        wait = WebDriverWait(self.browser, 30)
        elements = self.browser.find_element_by_xpath('/html/body/div[5]/div[2]/div[3]')
        print(elements.text)
        # for element in elements:
        #     print(element.text)
        self.browser.quit()

crawler = Crawler()
crawler.look_up()

