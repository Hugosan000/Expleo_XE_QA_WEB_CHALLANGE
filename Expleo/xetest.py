from behave import *
from selenium import webdriver
from tkinter import BROWSE
from allure_commons.types import AttachmentType
import  allure
import  pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then, given
#from features import tutorial


class TestXE:

        @given('The logo is visible')
        @allure.severity(allure.severity_level.MINOR)
        def test_visible_logo(self):
           
            self.driver=webdriver.Firefox()
            self.driver.get("https://www.xe.com")
            status=self.driver.find_element(By.CSS_SELECTOR,'h1.heading__Heading1-n07sti-0').is_displayed()
            if status==True:
                assert True
            else:
                assert False   
            self.driver.close() 
        
        @given('that the user can perform the conversion of 50 usd to GBP')
        @allure.severity(allure.severity_level.NORMAL)
        def test_sucessfull_50_USD_to_GBP(self):
            
            self.driver=webdriver.Firefox()
            self.driver.get("https://www.xe.com")
            self.driver.find_element(By.CSS_SELECTOR,'#amount').send_keys('50')
            self.driver.find_element(By.CSS_SELECTOR,'#midmarketFromCurrency').click
            self.driver.find_element(By.CSS_SELECTOR,'#midmarketFromCurrency').send_keys('USD',Keys.ENTER)
            self.driver.find_element(By.CSS_SELECTOR,'#midmarketToCurrency').send_keys('GBP',Keys.ENTER)
            self.driver.find_element(By.CSS_SELECTOR,'button.button__BaseButton-sc-1qpsalo-0:nth-child(3)').send_keys(Keys.ENTER)
            allure.attach(self.driver.get_screenshot_as_png(),name="Sucessfull 50 USD to GBP", 
            attachment_type=AttachmentType.PNG)

        @given('that the user can perform the conversion of 50 BRL to JPY') 
        @allure.severity(allure.severity_level.NORMAL)    
        def test_sucessfull_50_BRL_TO_JPY(self):
           
            self.driver=webdriver.Firefox()
            self.driver.get("https://www.xe.com")
            self.driver.find_element(By.CSS_SELECTOR,'#amount').send_keys('50')
            self.driver.find_element(By.CSS_SELECTOR,'#midmarketFromCurrency').click
            self.driver.find_element(By.CSS_SELECTOR,'#midmarketFromCurrency').send_keys('BRL',Keys.ENTER)
            self.driver.find_element(By.CSS_SELECTOR,'#midmarketToCurrency').send_keys('JPY',Keys.ENTER)
            self.driver.find_element(By.CSS_SELECTOR,'button.button__BaseButton-sc-1qpsalo-0:nth-child(3)').send_keys(Keys.ENTER)

        @given('the user cannot proceed if he enters words instead of numbers') 
        @allure.severity(allure.severity_level.NORMAL)
        def test_wordsinput_onnumbers_fields(self):
           
            self.driver=webdriver.Firefox()
            self.driver.get("https://www.xe.com")
            self.driver.find_element(By.CSS_SELECTOR,'#amount').send_keys('abc')
            self.driver.implicitly_wait(5)
            test = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/section/div[2]/div/main/form/div[1]/div[2]')
            print(test) 

        @given('that the user can perform the conversion of 50 GBP to ARS') 
        @allure.severity(allure.severity_level.NORMAL)
        def test_50GBP_to_ARS(self):
            
            self.driver=webdriver.Firefox()
            self.driver.get("https://www.xe.com")
            self.driver.find_element(By.CSS_SELECTOR,'#amount').send_keys('50')
            self.driver.find_element(By.CSS_SELECTOR,'#midmarketFromCurrency').click
            self.driver.find_element(By.CSS_SELECTOR,'#midmarketFromCurrency').send_keys('GBP',Keys.ENTER)
            self.driver.find_element(By.CSS_SELECTOR,'#midmarketToCurrency').send_keys('ARS',Keys.ENTER)
            
        



        
        @allure.severity(allure.severity_level.NORMAL)
        def test_swap_currencies(self):
           
            self.driver=webdriver.Firefox()
            self.driver.get("https://www.xe.com")
            self.driver.find_element(By.CSS_SELECTOR,'#amount').send_keys('50')
            self.driver.find_element(By.CSS_SELECTOR,'#midmarketFromCurrency').click
            self.driver.find_element(By.CSS_SELECTOR,'#midmarketFromCurrency').send_keys('BRL',Keys.ENTER)
            self.driver.find_element(By.CSS_SELECTOR,'#midmarketToCurrency').send_keys('JPY',Keys.ENTER)
            self.driver.find_element(By.CSS_SELECTOR,'.miscellany___StyledButton-sc-1r08bla-0').click()
            self.driver.find_element(By.CSS_SELECTOR,'button.button__BaseButton-sc-1qpsalo-0:nth-child(3)').click()
       


