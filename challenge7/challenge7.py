import time
import unittest
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.wait import WebDriverWait
from Challenge5 import helperMethods


class Challenge7(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../_drivers/chromedriver 79")

    def test_scrape_the_sites(self):
        car_sites_dict = []
        wait = WebDriverWait(self.driver, 20)

        self.driver.get('https://www.copart.com')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@ng-if='popularSearches']")))
        popular_array = self.driver.find_elements_by_xpath("//div[@ng-if='popularSearches']//ul/li/a")
        count = 0

        while count < len(popular_array):
            pair_list = []
            car_model = popular_array[count].text
            pair_list.append(car_model)

            href = popular_array[count].get_attribute("href")
            pair_list.append(href)

            # add pair_array to array of arrays
            car_sites_dict.append(pair_list)
            count += 1
        print(car_sites_dict)

        count = 0
        while count < len(car_sites_dict):
            pair = car_sites_dict[count]
            car_model = pair[0]
            car_site = pair[1]

            try:
                self.driver.get(car_site)
                self.driver.implicitly_wait(10)

                wait.until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "table#serverSideDataTable tbody")))
                body = self.driver.find_element_by_css_selector("table#serverSideDataTable tbody").text
                self.assertIn(car_model, body)

            except:
                screen_name = "{0}-{1}Error".format(car_model, car_site)
                self.driver.save_screenshot("{0}.png".format(screen_name))
                err = car_model + 'NotFound!'
                print('Error Thrown: ', err)
            count += 1

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()