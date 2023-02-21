import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Users\icefr\OneDrive\Desktop\Bootcamp SQA\Tugas17Sanbercode\chromedriver.exe')

    #login
    def login(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.NAME, 'user-name').send_keys('standard_user')
        time.sleep(2)
        driver.find_element(By.NAME, 'password').send_keys('secret_sauce')
        time.sleep(2)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(2)
        
    #logout
    def login(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.NAME, 'user-name').send_keys('standard_user')
        time.sleep(2)
        driver.find_element(By.NAME, 'password').send_keys('secret_sauce')
        time.sleep(2)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(2)
        driver.find_element(By.ID,"react-burger-menu-btn").click()
        time.sleep(2)
        driver.find_element(By.ID,"logout_sidebar_link").click()
        time.sleep(2)
        
    #login tanpa email dan password
    def login(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.NAME, 'user-name').send_keys('standard_user')
        time.sleep(2)
        driver.find_element(By.NAME, 'password').send_keys('secret_sauce')
        time.sleep(2)   
        driver.find_element(By.ID,"login-button").click()
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()