# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%
#how to update PATH library (usr/lib/bin) with new modules
import sys
sys.path.append('C:/Users/elot1z6/AppData/Local/Continuum/Anaconda3/Lib')

#%%s
#open browser to incognito 
from os import system
system("\"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe\" -incognito www.gmail.com")
system("\"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe\" -incognito www.soundcloud.com")

#%%
#https://sites.google.com/a/chromium.org/chromedriver/getting-started
import time
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/elot1z6/Documents/Python Scripts/Selenium/chromedriver/chromedriver.exe')

driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('Test')
search_box.submit()
time.sleep(5) # Let the user actually see something!
#driver.quit()
#%%
from selenium import webdriver
driver.set_window_size(1024, 600)
driver.maximize_window()

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(chrome_options=options)
#%%
#displays all python modules currently installed
import pip
installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
print(installed_packages_list)

#%%
#login to gmail

import requests
import BeautifulSoup

class SessionGoogle:
    def __init__(self, url_login, url_auth, login, pwd):
        self.ses = requests.session()
        login_html = self.ses.get(url_login)
        soup_login = BeautifulSoup(login_html.content).find('form').find_all('input')
        my_dict = {}
        for u in soup_login:
            if u.has_attr('value'):
                my_dict[u['name']] = u['value']
        # override the inputs without login and pwd:
        my_dict['Email'] = login
        my_dict['Passwd'] = pwd
        self.ses.post(url_auth, data=my_dict)

    def get(self, URL):
        return self.ses.get(URL).text
    
#function call
url_login = "https://accounts.google.com/ServiceLogin"
url_auth = "https://accounts.google.com/ServiceLoginAuth"
session = SessionGoogle(url_login, url_auth, "myGoogleLogin", "myPassword")
print (session.get("plus.google.com"))