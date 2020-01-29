import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class c2(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome("../_drivers/chromedriver 79")

    def tearDown(self):
        self.driver.quit()

    def test_porsche(self):

        searchterm = "exotic"
        self.driver.get("https://www.copart.com/")

        # Find the search field

        # Enter exotic in search field

        # Press enter

        # Wait for page to load

        # You knew you'd have to wait, how would we know you have to wait?

        # wouldn't this test assert anything in the table?  not just on the displayed page?  is this not the correct test?





        # self.driver.set_window_size(1200, 753)
        self.driver.execute_script("window.scrollTo(0,1)")
        searchfield = self.driver.find_element(By.ID, "input-search")
        searchfield.send_keys(searchterm)
        searchfield.send_keys(Keys.ENTER)

        time.sleep(5)
        dataelement = self.driver.find_element(By.XPATH, '//*[@id=\"serverSideDataTable\"]//tbody')
        html = dataelement.get_attribute("innerHTML")
        # self.assertIn("PORSCHE", html)


        # self.driver.find_element(By.ID, "input-search").send_keys("exotics")
        # self.driver.find_element(By.ID, "input-search").send_keys(Keys.ENTER)



        # driver.waituntil

        self.assertIn(searchterm, self.driver.title)

        results_table = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "serverSideDataTable_wrapper"))
        )

        # element = self.driver.find_element(By.ID, "serverSideDataTable_wrapper")
        # print(element.get_attribute("innerHTML"))

        assert "PORSCHE" in results_table.get_attribute("innerHTML")


if __name__ == '__main__':
    unittest.main()






        # self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) > td:nth-child(5) > span").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) > td:nth-child(5) > span").click()
        # element = self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) > td:nth-child(5) > span")
        # actions = ActionChains(driver)
        # actions.double_click(element).perform()
        # self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) > td:nth-child(5) > span").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) > td:nth-child(5) > span").click()
        # element = self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) > td:nth-child(5) > span")
        # actions = ActionChains(driver)
        # actions.double_click(element).perform()
        # self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) > td:nth-child(5) > span").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) .imgpath img").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".col-sm-12 > div > .row .title").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".col-sm-12 > div > .row .title").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".col-sm-12 > div > .row .title").click()
        # element = self.driver.find_element(By.CSS_SELECTOR, ".col-sm-12 > div > .row .title")
        # actions = ActionChains(driver)
        # actions.double_click(element).perform()

