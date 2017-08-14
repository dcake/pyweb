#!/usr/bin/env python3
# coding:utf-8


import unittest
from selenium import webdriver
import time


class Test(unittest.TestCase):
    """
    test selenium api
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://chandao.cyjysoft.com/"
        self.driver.implicitly_wait(5)

    def testClick(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("zentao").click()
        driver.find_element_by_name("account").clear()
        driver.find_element_by_name("account").send_keys("liumeng")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("liumeng")
        driver.find_element_by_id("submit").click()
        time.sleep(2)

        # 断言
        self.assertEqual(u"我的地盘 - 禅道", driver.title)
        # print(driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
