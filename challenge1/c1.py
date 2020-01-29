import unittest
from selenium import webdriver

class challenge1(unittest.TestCase):

    name = "Matt"
    cool = False

    def setUp(self):
        self.driver = webdriver.Chrome("../_drivers/chromedriver 79")
        #code to startup webdriver

    def tearDown(self):
         self.driver.close()
        # code to close webdriver

    def test_challenge1(self):
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)

    def test_challenge2(self):
        self.driver.get("https://www.amazon.com")
        self.assertIn("Amazon", self.driver.title)

    # def test_challenge3(self):
    #     print('go to XANT')
    #     self.driver.get("https://www.xant.ai")
    #     self.assertIn("Home - XANT", self.driver.title)

    def test_challenge4(self):
        self.driver.get("https://www.msn.com")
        self.assertIn("MSN", self.driver.title)

if __name__ == '__main__':
    unittest.main()