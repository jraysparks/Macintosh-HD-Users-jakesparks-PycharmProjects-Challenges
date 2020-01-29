import time

import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class test_younique_cart(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome("../_drivers/chromedriver")

    def tearDown(self):
        self.driver.quit()

    def test_younique_site(self):

        self.driver.get("https://www.youniqueproducts.com/products/view/US-51081-01")
        self.assertIn("Younique", self.driver.title)




    # add the item to the cart

        self.driver.find_element(By.CSS_SELECTOR, "[class*='addToCartBtn']").click()

    # go to Cart

        self.driver.find_element(By.CSS_SELECTOR, "[class*='icon-cart']").click()

    # validate the cart overview

        # webelements = self.driver.find_elements(By.CSS_SELECTOR, "[class*='totalDisplay']")

        # webelements = self.driver.find_elements(By.XPATH, "//*[@id='cartview']//tbody//*[contains(@class,'total')]")

        webelements = self.driver.find_elements(By.XPATH, "//*[@id='cartview']//td[contains(@class, 'total')]")

        time.sleep(2)

        # dict = {}
        #
        # for i in range(2, len(webelements) - 2, 2):
        #     dict[webelements[i].text] = webelements[i + 1].text
        # print(dict)



        counter = 0
        for x in webelements:
            print(x.text)
            counter += 1
            if x.text == "Total Items:":
                print(f"counter: {counter}")
                print(f"webelement: ########{webelements[counter].text}hi")
                assert webelements[counter].text == "1"
            if x.text == "Subtotal:":
                print(f"counter: {counter}")
                print(f"webelement: ########{webelements[counter].text}hi")
                assert webelements[counter].text == "$12.00"
            if x.text == "Shipping:":
                print(f"counter: {counter}")
                print(f"webelement: ########{webelements[counter].text}hi")
                assert webelements[counter].text == "$5.50"
            if x.text == "Total Balance Due:":
                print(f"counter: {counter}")
                print(f"webelement: ########{webelements[counter].text}hi")
                assert webelements[counter].text == "$17.50 USD"










        # for x in webelements:
        #     print(x.get_attribute("innerHTML") + " " + "-" + " " + x.get_attribute("href"))
        #

        # webelements = self.driver.find_elements(By.XPATH, "//*[@ng-if=\"popularSearches\"]//a")
        # webelements.sort()
        # for x in webelements:
        #     # print(x.get_attribute("innerHTML") + " " + "-" + " " + x.get_attribute("href"))
        #     # print(f"{x.get_attribute('innerHTML')} - {x.get_attribute('href')}")
        #     print(f"{x.text} - {x.get_attribute('href')}")


    # def test_challenge3WhileLoop(self):
    #     self.driver.get("https://www.copart.com/")
    #     webelements = self.driver.find_elements(By.XPATH, "//*[ng-if=\"popularSearches\"]/../div[3]//li/a")
    #
    #     count = 0
    #     print (len(webelements))
    #     while count < len(webelements):
    #         print(webelements[count].text + " - " + webelements[count].get_attribute("href"))
    #         count = count + 1


if __name__ == '__main__':
    unittest.main()



