import time
import requests
import sys
import re
from lxml import html
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class VoteScraper:
    def __init__(self):
        options = Options()
        # options.add_argument("--headless")
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-gpu')
        options.add_argument("--disable-notifications")
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument('--hide-scrollbars')
        options.add_argument("--log-level=3")
        # Chrome Driver - https://sites.google.com/a/chromium.org/chromedriver/home
        self.driver = webdriver.Chrome(chrome_options=options)
        self.wait = WebDriverWait(self.driver, 300)

    def get_links(self, max_company_count=1000):
           try:
              self.driver.get('https://mycutebaby.in/contest/participant/?n=5ec6c4189c667&utm_source=wsapp_share&utm_campaign=May_2020&utm_medium=shared&utm_term=wsapp_shared_5ec6c4189c667&utm_content=participant')
              self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.voter_details")))
              self.driver.find_element_by_name('v').send_keys('Ravindra Prajapati')
              self.driver.find_element_by_id('vote_btn').click()
              time.sleep(60) 
           except Exception as e:
               self.get_log(e, 'Exception', 'get_links function')
               print(e)
           
           finally:
               self.driver.close()
               self.driver.quit()

           return "Executed Func()"


if __name__ == '__main__':
    scraper = VoteScraper()

    company_links = scraper.get_links(max_company_count=100)
    print("Scraping Done!")