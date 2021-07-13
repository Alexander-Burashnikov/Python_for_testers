# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class SearchBruhTest(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome('C:\\Windows\\SysWOW64\\chromedriver.exe')
        #self.wd.get("http://www.google.com")
        self.wd.implicitly_wait(30)
    
    def test_search_bruh(self):
        wd = self.wd
        #Open home page
        wd.get("https://www.google.com/search?q=bruh+meme&rlz=1C1GCEA_enRU956RU956&oq=bruh+meme&aqs=chrome..69i57j0l9.2039j0j7&sourceid=chrome&ie=UTF-8")
        #Open google images
        wd.find_element_by_link_text(u"Картинки").click()
        #Watching images
        wd.find_element_by_xpath(u"//img[@alt='Брух — Что это значит? Мемы | AntiSlang.ru']").click()
        wd.find_element_by_xpath("//img[@alt='BRUH MEMES (@BRUH64122310) | Twitter']").click()
        wd.find_element_by_xpath("//img[@alt='Like bruh: memes']").click()
        wd.find_element_by_xpath("//div[@id='Sva75c']/div/div/div[3]/div[2]/c-wiz/div/div/div[3]/div/a/div").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        wd.close()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
    
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
