import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class c3(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome("../_drivers/chromedriver 79")

    def tearDown(self):
        self.driver.quit()

    def test_challenge3(self):

        self.driver.get("https://www.copart.com/")

        # webelements = self.driver.find_elements(By.XPATH, "//*[@ng-if=\"popularSearches\"]//a")
        # for x in webelements:
        #     print(x.get_attribute("innerHTML") + " " + "-" + " " + x.get_attribute("href"))
        #

        webelements = self.driver.find_elements(By.XPATH, "//*[@ng-if=\"popularSearches\"]//a")
        # webelements.sort()
        for x in webelements:
            # print(x.get_attribute("innerHTML") + " " + "-" + " " + x.get_attribute("href"))
            # print(f"{x.get_attribute('innerHTML')} - {x.get_attribute('href')}")
            print(f"{x.text} - {x.get_attribute('href')}")


    def test_challenge3WhileLoop(self):
        self.driver.get("https://www.copart.com/")
        webelements = self.driver.find_elements(By.XPATH, "//*[ng-if=\"popularSearches\"]/../div[3]//li/a")

        count = 0
        print(len(webelements))
        while count < len(webelements):
            print(webelements[count].text + " - " + webelements[count].get_attribute("href"))
            count = count + 1





        #
        # i = 0
        # while i < webelements.count():
        #     print(i)
        #     i += 1


        # def test_challenge3(self):

        # self.driver.get('https://www.copart.com/')
        # webelements = self.driver.find_elements_by_xpath('//*[@id="tabTrending"]//ul//li')
        # print(webelements)

        # element.text
        # element.getAttribute("href")
        #
        # <div id="jake">
        # element.getAttribute(id) => jake
        #

        # print("Hi")
        # print(html)
        #
        # fruits = ["apple", "banana", "cherry"]
        # for x in fruits:
        #     print(x)
















        # searchterm = "exotic"
        # self.driver.get("https://www.copart.com/")

        # Find the search field

        # Enter exotic in search field

        # Press enter

        # Wait for page to load

        # You knew you'd have to wait, how would we know you have to wait?

        # wouldn't this test assert anything in the table?  not just on the displayed page?  is this not the correct test?





        # self.driver.set_window_size(1200, 753)
        # self.driver.execute_script("window.scrollTo(0,1)")
        # searchfield = self.driver.find_element(By.ID, "input-search")
        # searchfield.send_keys(searchterm)
        # searchfield.send_keys(Keys.ENTER)
        #
        # time.sleep(5)
        # dataelement = self.driver.find_element(By.XPATH, '//*[@id=\"serverSideDataTable\"]//tbody')
        # html = dataelement.get_attribute("innerHTML")
        # self.assertIn("PORSCHE", html)


        # self.driver.find_element(By.ID, "input-search").send_keys("exotics")
        # self.driver.find_element(By.ID, "input-search").send_keys(Keys.ENTER)



        # driver.waituntil

        # self.assertIn(searchterm, self.driver.title)
        #
        # results_table = WebDriverWait(self.driver, 15).until(
        #     EC.presence_of_element_located((By.ID, "serverSideDataTable_wrapper"))
        # )

        # element = self.driver.find_element(By.ID, "serverSideDataTable_wrapper")
        # print(element.get_attribute("innerHTML"))

        # assert "PORSCHE" in results_table.get_attribute("innerHTML")


if __name__ == '__main__':
    unittest.main()



