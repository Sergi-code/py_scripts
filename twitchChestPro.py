from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.youradress.org")#put here the adress of your page
elem = driver.find_elements_by_xpath("//*[@type='submit']")#put here the content you have put in Notepad, ie the XPath
button = driver.find_element_by_id('buttonID')
print(elem.get_attribute("class"))
driver.close()