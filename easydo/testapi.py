#!/usr/bin/env python3
# coding:utf-8

# from easydo.DateHelper import DateHelper as DH
from xml.etree import cElementTree as cET

etree = cET.parse("../testdate/user.xml")
ss = etree.findall("date")
s1 = etree.getroot()
# s2 = etree.find("username")
s2 = etree.getiterator("date")
print(ss,s1, s2)


