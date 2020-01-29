import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class Challenge6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../_drivers/chromedriver 79")
        self.driver.get("https://www.copart.com/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_error_handling(self):
        wait = WebDriverWait(self.driver, 20)

        #Search for Nissan
        search_input = wait.until(ec.presence_of_element_located((By.ID, "input-search")))
        search_input.click()
        search_input.send_keys("Nissan")
        self.driver.find_element_by_css_selector('[data-uname="homepageHeadersearchsubmit"]').click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "table#serverSideDataTable tbody")))
        self.assertIn("Nissan", self.driver.title)

        #Get Model Filter
        model_filter = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@data-uname="ModelFilter"]')))
        model_filter.click()

        #Try Catch for Skyline
        try:
            model_search = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="collapseinside4"]/form/div/input')))
            model_search.send_keys('skyline')

            # // *[ @ id = "filters-collapse-1"] / div[1] / ul / li[4] / h4 / a[1] / i

            self.driver.find_element_by_xpath("//*[@id='lot_model_descSKYLINE']").click()
            wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, '[data-uname="lotsearchLotmodel"]'), "SKYLINE"))

            model = self.driver.find_element_by_css_selector('[data-uname="lotsearchLotmodel"]')
            model_name = model.get_attribute('innerText')
            self.assertIn("SKYLINE", model_name)
            self.driver.save_screenshot("screenshot.png")
            print("Skyline is Available! Buy now :)")

        except:
            print('::Error:: SKYLINE NOT FOUND')
            self.driver.save_screenshot("screenshot.png")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()