#!/usr/bin/env python3
# conding:utf-8
"""
页面基本操作，封装selenium常用方法
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class WebHelper(object):
    """
    封装selenium api
    简化页面重复操作
    """
    # global driver

    def __init__(self, btype="close", atype="chrome", ctype="local"):
        """
        constructor构造器，用于初始化一些操作
        :param atype:选择浏览器类型
        :param btype:开关参数
        :param ctype:使用本地／远程浏览器
        """
        if btype == "open":
            if atype == "chrome":
                if ctype == "local":
                    self.driver = webdriver.Chrome()
                    self.driver.maximize_window()
                elif ctype == "notlocal":
                    self.driver = webdriver.Remote(command_executor="http://124.65.151.158:4444/wd/hub",
                                                   desired_capabilities=webdriver.DesiredCapabilities.CHROME)
                    self.driver.maximize_window()
            elif atype == "firefox":
                if ctype == "local":
                    self.driver = webdriver.Firefox
                    self.driver.maximize_window()
                elif ctype == "notlocal":
                    self.driver = webdriver.Remote(command_executor="http://124.65.151.158:4444/wd/hub",
                                                   desired_capabilities=webdriver.DesiredCapabilities.FIREFOX)
                    self.driver.maximize_window()
            elif atype == "ie":
                if ctype == "local":
                    self.driver = webdriver.Ie()
                    self.driver.maximize_window()
                elif ctype == "notlocal":
                    self.driver = webdriver.Remote(command_executor="http://124.65.151.158:4444/wd/hub",
                                                   desired_capabilities=webdriver.DesiredCapabilities.INTERNETEXPLORER)
                    self.driver.maximize_window()

        # DRIVER = self.driver

    def get_element(self, findby, byvalue):
        """
        获取页面元素，供后面操作使用
        :param findby: 定位方式
        :param byvalue: 要定位的元素的值
        :return:
        """
        if findby == "byid":
            self.driver.find_element_by_id(byvalue)
        elif findby == "byname":
            self.driver.find_element_by_name(byvalue)
        elif findby == "byxpath":
            self.driver.find_element_by_xpath(byvalue)
        elif findby == "byclassname":
            self.driver.find_element_by_class_name(byvalue)
        elif findby == "bylinktext":
            self.driver.find_element_by_link_text(byvalue)
        elif findby == "bypartiallinktext":
            self.driver.find_element_by_partial_link_text(byvalue)

    def click(self, findby, byvalue):
        """
        页面按钮点击操作
        :param findby: 定位方式
        :param byvalue: 要定位元素的值
        :return:
        """
        if findby == "byid":
            self.driver.find_element_by_id(byvalue).click()
        elif findby == "byname":
            self.driver.find_element_by_name(byvalue).click()
        elif findby == "byxpath":
            self.driver.find_element_by_xpath(byvalue).click()
        elif findby == "byclassname":
            self.driver.find_element_by_class_name(byvalue).click()
        elif findby == "bylinktext":
            self.driver.find_element_by_link_text(byvalue).click()
        elif findby == "bypartiallinktext":
            self.driver.find_element_by_partial_link_text(byvalue).click()

    def double_click(self, findby, byvalue):
        """
        页面双击操作
        :param findby: 定位方式
        :param byvalue: 要定位元素的值
        :return:
        """
        chain = ActionChains(self.driver)
        if findby == "byid":
            element = self.driver.find_element_by_id(byvalue)
            chain.double_click(element).perform()
        elif findby == "byname":
            element = self.driver.find_element_by_name(byvalue)
            chain.double_click(element).perform()
        elif findby == "byxpath":
            element = self.driver.find_element_by_xpath(byvalue)
            chain.double_click(element).perform()
        elif findby == "byclassname":
            element = self.driver.find_element_by_class_name(byvalue)
            chain.double_click(element).perform()

    def input_value(self, findby, byvalue, value):
        """
        页面文本输入
        :param findby: 定位方式
        :param byvalue: 要定位元素的值
        :param value: 要输入的值 | 此处如果传入文件路径，可实现上传文件功能，最好将文件与代码放至一起。
        :return:
        """
        if findby == "byid":
            # self.driver.find_element_by_id(byvalue).clear()
            self.driver.find_element_by_id(byvalue).send_keys(value)
        elif findby == "byname":
            # self.driver.find_element_by_name(byvalue).clear()
            self.driver.find_element_by_name(byvalue).send_keys(value)
        elif findby == "byxpath":
            # self.driver.find_element_by_xpath(byvalue).clear()
            self.driver.find_element_by_xpath(byvalue).send_keys(value)
        elif findby == "byclassname":
            # self.driver.find_element_by_class_name(byvalue).clear()
            self.driver.find_element_by_class_name(byvalue).send_keys(value)

    def selecter(self, findby, byvalue, value):
        """
        页面下拉框内容选择
        :param findby:
        :param byvalue:
        :param value:
        :return:
        """
        if findby == "byid":
            select = Select(self.driver.find_element_by_id(byvalue))
            select.select_by_visible_text(value)
        elif findby == "byname":
            select = Select(self.driver.find_element_by_name(byvalue))
            select.select_by_visible_text(value)
        elif findby == "byxpath":
            select = Select(self.driver.find_element_by_xpath(byvalue))
            select.select_by_visible_text(value)
        elif findby == "byclassname":
            select = Select(self.driver.find_element_by_class_name(byvalue))
            select.select_by_visible_text(value)

    def get_text(self, findby, byvalue):
        """
        获取页面元素的text值
        :param findby: 定位方式
        :param byvalue: 要定位的元素的值
        :return: 返回元素text内容
        """
        if findby == "byif":
            return self.driver.find_element_by_id(byvalue).text
        elif findby == "byname":
            return self.driver.find_element_by_name(byvalue).text
        elif findby == "byxpath":
            return self.driver.find_element_by_xpath(byvalue).text
        elif findby == "byclassname":
            return self.driver.find_element_by_class_name(byvalue).text

    def new_tab(self, clickelement):
        # ele = self.driver.find_element_by_tag_name("body")
        # ele.send_keys(Keys.CONTROL + "t")
        # # self.driver.switch_to.window()
        actions = ActionChains(self.driver)
        ele = self.driver.find_element_by_id(clickelement)
        actions.key_down(Keys.COMMAND).click(ele).key_up(Keys.COMMAND).perform()

    def switch_to_window(self):
        pass

    def get_url(self, url):
        self.driver.get(url)

    def tear_down(self):
        self.driver.quit()

    def wait_element(self, waittime):
        self.driver.implicitly_wait(waittime)
