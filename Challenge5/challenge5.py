import time
import unittest
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.wait import WebDriverWait
from Challenge5 import helperMethods



class Challenge5(unittest.TestCase) :
    def setUp (self):
        print('In setup method.')
        self.driver = webdriver.Chrome("../_drivers/chromedriver 79")
    def test_challenge5 (self) :
        site = "https://www.copart.com"
        driver = self.driver
        driver.maximize_window()
        wait = WebDriverWait(driver, 15)
        # 1. Open up Copart
        print('Go to Copart.com')
        driver.get(site)
        # 2. Search for Porsche
        print('Search for Exotics')
        element = driver.find_element(By.ID, "input-search")
        element.send_keys(("Porsche" + Keys.ESCAPE))
        time.sleep(2)
        element.send_keys(Keys.ENTER)
        WebDriverWait(driver, 5).until(EC.title_contains('Porsche'))
        #3. Wait for Spinner
        # pspinner = driver.find_element(By.ID, "serverSideDataTable_processing")
        # wait.until(lambda _: pspinner.get_attribute('style') == 'display: block;')
        # wait.until(lambda _: pspinner.get_attribute('style') == 'display: none;')
        # 3. Increase selected count from 20 to 100
        element = driver.find_element(By.XPATH, '//select[@name="serverSideDataTable_length"]')
        element.click()
        element.send_keys("100")
        element.send_keys(Keys.ENTER)
        # element.click()
        #4. Wait for Spinner

        # pspinner = driver.find_element(By.ID, "serverSideDataTable_processing")
        # wait.until(lambda _: pspinner.get_attribute('style') == 'display: block;')
        # wait.until(lambda _: pspinner.get_attribute('style') == 'display: none;')

        # 5. Count how many different models of porsche on first page and return in terminal
        models = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@data-uname="lotsearchLotmodel"]')))
        model_list = []
        for item in models:
            if item.text != ' ':
                model_name = item.text
                model_list.append(model_name)
        sorted_list = sorted(model_list)
        model_dict = {}
        for car_model in sorted_list:
            helperMethods.add_pair(car_model, model_dict)
        print('********* Model Count ************')
        for model in model_dict:
            count = model_dict[model]
            print('{0}-{1}'.format(model, count))
        #Report Damages
        hits = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@data-uname="lotsearchLotdamagedescription"]')))
        dmg_dict = {}
        for dmg in hits:
            if dmg.text != ' ':
                dmg_name = dmg.text
                if dmg_name == "FRONT END":
                    helperMethods.add_pair(dmg_name, dmg_dict)
                elif dmg_name == "REAR END":
                    helperMethods.add_pair(dmg_name, dmg_dict)
                elif dmg_name == "MINOR DENT/SCRATCHES":
                    helperMethods.add_pair(dmg_name, dmg_dict)
                elif dmg_name == "UNDERCARRIAGE":
                    helperMethods.add_pair(dmg_name, dmg_dict)
                else:
                    helperMethods.add_pair("MISC", dmg_dict)
        print('*************** DAMAGE COUNT *******************')
        for dmg in dmg_dict:
            count = dmg_dict[dmg]
            print('{0} - {1}'.format(dmg, count))
    def tearDown(self):
        self.driver.close()
        print('In close method.')

if __name__ == '__main__':
    unittest.main()