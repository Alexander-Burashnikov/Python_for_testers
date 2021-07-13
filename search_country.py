# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, time

class SearchCountry(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome("C:\\Windows\\SysWOW64\\chromedriver.exe")
        self.wd.implicitly_wait(1000)
    
    def test_search_country(self):
        wd = self.wd
        self.search_wikipedia(wd, "https://www.google.com/search?q=%D0%B2%D0%B8%D0%BA%D0%B8%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F&rlz=1C1GCEA_enRU956RU956&oq=%D0%B2%D0%B8%D0%BA%D0%B8%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F&aqs=chrome.0.69i59j0l3j46j69i61l3.2742j0j7&sourceid=chrome&ie=UTF-8")
        self.open_wikipedia(wd)
        self.search_chili(wd, u"чили")
        self.watch_chili(wd)
        self.search_argentina(wd, u"аргентина")
        self.watch_argentina(wd)
        wd.close()

    def search_argentina(self, wd, input):
        wd.find_element_by_id("searchInput").click()
        time.sleep(1)
        wd.find_element_by_id("searchInput").clear()
        time.sleep(1)
        wd.find_element_by_id("searchInput").send_keys(input)
        time.sleep(1)
        wd.find_element_by_id("searchform").submit()
        time.sleep(1)

    def watch_argentina(selfself, wd):
        wd.find_element_by_xpath("//div[@id='toc']/ul/li[2]/a/span[2]").click()
        time.sleep(1)

    def watch_chili(self, wd):
        wd.find_element_by_xpath("//div[@id='toc']/ul/li[6]/a/span[2]").click()
        time.sleep(1)
        wd.find_element_by_xpath("//div[@id='toc']/ul/li[2]/a/span[2]").click()
        time.sleep(1)
        wd.find_element_by_xpath("//img[@alt='Lonquimay-85-k.jpg']").click()
        time.sleep(1)
        wd.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Заявление о куки'])[1]/following::button[4]").click()
        time.sleep(1)
        wd.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Заявление о куки'])[1]/following::button[4]").click()
        time.sleep(1)
        wd.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Заявление о куки'])[1]/following::button[1]").click()
        time.sleep(1)

    def search_chili(self, wd, input):
        wd.find_element_by_id("searchInput").click()
        time.sleep(1)
        wd.find_element_by_id("searchInput").clear()
        time.sleep(1)
        wd.find_element_by_id("searchInput").send_keys(input)
        time.sleep(1)
        wd.find_element_by_id("searchform").submit()
        time.sleep(1)

    def open_wikipedia(self, wd):
        wd.find_element_by_xpath("//div[@id='rso']/div/div/div/div/div/div/div/a/h3").click()

    def search_wikipedia(self, wd, link):
        wd.get(link)

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
