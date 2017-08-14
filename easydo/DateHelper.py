#!/usr/bin/env python3
# coding:utf-8

import MySQLdb
from xml.dom import minidom


global DOC, CONN


class DateHelper(object):
    """
    数据操作类
    """
    def __init__(self, filename):
        """
        初始化xml文档
        """
        global DOC, CONN
        DOC = minidom.parse("../testdate/"+filename)

    def read_xml(self, ftagname, num, stagname):
        """
        从指定文件中，读取指定节点的值
        :param ftagname:起始节点的名字
        :param num:取与起始节点相同的第num个节点
        :param stagname:起始节点下的二级节点
        :return:返回二级节点的值
        """
        root = DOC.documentElement
        msg = root.get