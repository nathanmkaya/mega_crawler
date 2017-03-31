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
            self.browser.get("https://www.alamo.de/Locations/732/de")

    @contextmanager
    def wait_for_page_load(self, element ,timeout=30):
        yield
        WebDriverWait(self.browser, timeout).until(staleness_of(element))

    def look_up(self):
        wait = WebDriverWait(self.browser, 30)
        select_country = Select(wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#country'))))
        countries = [i.text for i in select_country.options if i != select_country.first_selected_option]
        with self.wait_for_page_load(select_country):
            for country in countries:
                Select(self.browser.find_element_by_css_selector('#country')).select_by_visible_text(country)
                select_place = Select(self.browser.find_element_by_xpath('//*[@id="pickup"]'))
                places = [i.text for i in select_place.options if i != select_place.first_selected_option]
                for place in places:
                    Select(self.browser.find_element_by_xpath('//*[@id="pickup"]')).select_by_visible_text(place)
                    print(country + " : " + place)
                    self.browser.find_element_by_name('formButton[portallocations_searchresult_component][Search]').click()
                    result = self.browser.find_element_by_xpath(".//*[@id='page-main']/table/tbody/tr/td/div/table/tbody/tr[2]/td[2]/table/tbody")
                    print(result.text)
                self.browser.refresh()
        self.browser.quit()

crawler = Crawler()
crawler.look_up()



