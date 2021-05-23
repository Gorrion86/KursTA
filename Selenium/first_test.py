from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/kamil/PycharmProjects/taps_git/Drivers/chromedriver.exe')

url = 'https://google.pl'

driver.get(url)

searchbox = driver.find_element_by_name('q')

searchbox.send_keys('selenium python')

searchbox.submit()

time.sleep(5)

driver.quit()