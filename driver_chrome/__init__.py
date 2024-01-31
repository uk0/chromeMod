
import os
import random
from concurrent import futures

from selenium.webdriver.common import by
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

import xxhash
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import requests
import json



def extract_tag_content(tag, content):
    pattern = f'<{tag}>(.*?)</{tag}>'
    return re.findall(pattern, content, re.DOTALL)


class SearchGoogle(object):
    def __init__(self):
        self.driver = None
        self.session = requests.session()
        self.is_debugger = os.environ.get('IS_DEBUG', 'false')
        self.cnf = webdriver.ChromeOptions()

        # 设置代理
        user_agent = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                      "Version/12.0.3 Safari/605.1.15")
        # self.cnf.add_argument("--headless")
        # self.cnf.add_argument("--no-sandbox")
        self.cnf.add_argument("--disable-dev-shm-usage")
        self.cnf.add_argument('--user-agent=%s' % user_agent)
        prefs = {"download.default_directory": "/tmp/"}
        self.cnf.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(options=self.cnf)
        self.driver.set_window_size(1920, 1080)
        self.driver.get("https://www.google.com/")
        wait = WebDriverWait(self.driver, 30)
        # 等待表格组件加载完毕
        wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/center/form/table/tbody/tr/td[2]/div/input")))

    def query_to_list_result_data(self,msg,search_number_page):
        # //*[@id="APjFqb"]
        input = self.driver.find_element(By.XPATH,value="/html/body/center/form/table/tbody/tr/td[2]/div/input")
        input.send_keys(msg)
        input.send_keys("\r\n")
        print("send keys")

    def get_page_data(self):
        search_result = self.driver.find_element(By.XPATH,'//*[@id="main"]')
        results = search_result.find_elements(By.TAG_NAME,"div")
        for i in results:
            print("==========================================")
            print(i.text)



if __name__ == '__main__':
    test = SearchGoogle()
    test.query_to_list_result_data("你好",2)
    test.get_page_data()
    sleep(100000)

