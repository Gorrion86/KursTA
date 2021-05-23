from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome('C:/Users/kamil/PycharmProjects/taps_git/Drivers/chromedriver.exe')
elem = WebDriverWait

url = 'https://fabrykatestow.pl/'

driver.get(url)

driver.find_element_by_id('menu-item-622').click()

driver.find_element_by_xpath('//*[@id="content"]/div/div/div/section/div[2]/div/div/div/div/section[1]/div/div/div[1]/div/div/div/div/div/a').click()

elem = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div/div/div/section[5]/div[1]')
move = ActionChains(driver).move_to_element(elem)
move.perform()

elem.screenshot('test.png')