from behave import *
from selenium import webdriver
import  pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@then('clicking on Convert button the expect result about the conversion should appears  ****{float}')
def step_then(self) :
            self.driver=webdriver.Firefox()
            self.driver.get("https://www.xe.com")
            self.driver.find_element(By.CSS_SELECTOR,'#amount').send_keys('50')
            self.driver.find_element(By.CSS_SELECTOR,'#midmarketFromCurrency').click
            self.driver.find_element(By.CSS_SELECTOR,'#midmarketFromCurrency').send_keys('USD',Keys.ENTER)
            self.driver.find_element(By.CSS_SELECTOR,'#midmarketToCurrency').send_keys('GBP',Keys.ENTER)
            self.driver.find_element(By.CSS_SELECTOR,'button.button__BaseButton-sc-1qpsalo-0:nth-child(3)').send_keys(Keys.ENTER)
            
