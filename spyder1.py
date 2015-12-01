# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 21:22:15 2015

@author: milk1989
"""

from selenium import webdriver
import time

class WebTest(object):
    #this is web test class    
    def __init__(self,url_name):  #url name is a property
        self.url_name = url_name;
    
    def get_web(self):
        browser = webdriver.Chrome() #open chrome
        browser.get(self.url_name) #get url
    
web1 = WebTest("www.baidu.com")
web1.get_web()