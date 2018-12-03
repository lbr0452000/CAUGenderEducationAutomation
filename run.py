# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import os
import sys
os.path.dirname(os.path.abspath(sys.argv[0]))

ID = input("ID : ")
PW = input("PW : ")

driver = webdriver.Chrome(os.path.dirname(os.path.abspath(sys.argv[0]))+'/chromedriver')
driver.implicitly_wait(3)
driver.get('https://genderedu.cau.ac.kr/index.php?mid=m03')
driver.find_element_by_name('userID').send_keys(ID)
driver.find_element_by_name('password').send_keys(PW)
driver.find_element_by_xpath("//input[@title='로그인']").click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

for url in soup.find_all("a", {"class":"button icon play"}):
    url = url["onclick"].replace("Javascript: open_cwindow('course', '/gen_edu.php?mid=m03&pact=course&uid=", "")
    url = url.replace("', 0,0,800,650,0,0,0,1,1); return false;", "")
    url = "https://genderedu.cau.ac.kr/gen_edu.php?mid=m03&pact=course&uid="+url

    driver.execute_script('window.open("'+url+'","_blank");')
    driver.switch_to.window(driver.window_handles[len(driver.window_handles)-1])
    driver.find_element_by_tag_name("iframe").send_keys(" ")

    WebDriverWait(driver, 400).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.accept()
    driver.switch_to.window(driver.window_handles[0])