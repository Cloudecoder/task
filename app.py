from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.youtube.com/')
time.sleep(4)

trailer_name = 'The Pursuit of Happyness'

search = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox')
search.send_keys(trailer_name)

driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button').click()
time.sleep(4)

title = driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
title.click()
print(title.text)
