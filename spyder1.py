# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 21:22:15 2015

@author: milk1989
"""

from selenium import webdriver
import time

browser = webdriver.Firefox() #open chrome

class WebTest(object):
    #this is web test class    
    def __init__(self,url_name):  #url name is a property
        self.url_name = url_name;
        browser.get(self.url_name) #get url
    #set up sheep time 
    def sheep(self,sheep_time):  
        sheep_time = sheep_time
        time.sleep(sheep_time)
    # by id
    def find_element_by_id_sendkeys(self,name,context):
        id_name = name
        text = context
        browser.find_element_by_id(id_name).send_keys(text)
        
   # by name
    def find_element_by_name_sendkeys(self,name,context):
        name = name
        browser.find_element_by_name(name)
        
    #by link text
    def find_element_by_link_text(self,text_name):
        name = text_name 
        browser.find_element_by_link_text(name)
        
    #bu  x_path
    def find_element_by_path(self,text_name):
        name = text_name 
        browser.find_element_by_xpath(name) 
        
     #close web  
    def web_close(self):
        browser.close();
        
class method(WebTest):
    """sub class of webtest"""
    def click(self):
        
web1 = WebTest("http://www.baidu.com")
web1.find_element_by_id_sendkeys("kw","selenium").m
web1.sheep(20)
web1.web_close()
web1.m
