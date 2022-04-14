from selenium import webdriver
from time import sleep

my_driver = webdriver.Chrome()
my_driver.get("https://github.com")
sleep(5)
my_driver.refresh()
sleep(3)
my_driver.close()

