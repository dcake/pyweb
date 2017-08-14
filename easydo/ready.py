#!/usr/bin/env python3
# coding:utf-8

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

baidu = r"http://www.baidu.com/"
chandao = r"http://chandao.cyjysoft.com/"
mail = r"http://mail.cyjysoft.com/"

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get(mail)
ele = driver.find_element_by_partial_link_text(u"管理员")
# 打开新tab页
for i in range(2):
    ActionChains(driver).key_down(Keys.COMMAND).click(ele).key_up(Keys.COMMAND).perform()
    print(driver.current_window_handle)

driver.find_element_by_id("qquin").send_keys("liumeng@cyjysoft.com")
driver.find_element_by_id("pp").send_keys("Cyjy007")

# # chandao
# driver.switch_to.window(driver.current_window_handle[1])
# driver.get(chandao)
# driver.find_element_by_id("zentao").click()
# driver.find_element_by_id("account").send_keys("liumeng")
# driver.find_element_by_name("password").send_keys("liumeng")
# driver.find_element_by_id("submit").click()

# baidu
driver.switch_to.window(driver.current_window_handle[-1])
driver.get(baidu)
time.sleep(3)




# js2 = 'window.open("http://chandao.cyjysoft.com/");'
# js3 = 'window.open("http://mail.cyjysoft.com/");'
# driver = webdriver.Chrome()
# driver.get(url1)
# driver.execute_script(js2)
# driver.execute_script(js3)
#
# handles = driver.window_handles
# # driver.switch_to.window(handles[1])
# # print(handles)
# for hd in handles:
#     if hd != driver.current_window_handle:
#         pass
