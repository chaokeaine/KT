from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://192.168.1.246:8443/CDGServer3/index.jsp")
driver.maximize_window()
sleep(3)

driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[3]/td[3]/input').send_keys('systemadmin')
driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[5]/td[3]/input').send_keys('12345678')
driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[7]/td[3]/a[1]/img').click()
sleep(3)
dd = driver.find_element_by_xpath('//*[@id="oa_left_middle"]')
driver.switch_to.frame(dd)
driver.find_element_by_xpath('//*[@id="0001000000011"]').click()
sleep(2)
driver.switch_to.default_content()
ff = driver.find_element_by_xpath('//*[@id="oa_main"]')
driver.switch_to.frame(ff)
iframes = driver.find_element_by_xpath('//*[@id="frmUserList"]')
driver.switch_to.frame(iframes)
driver.find_element_by_xpath('//*[@id="tbUserList"]/thead[2]/tr/td/input[3]').click()
sleep(2)

driver.switch_to.default_content()
hh = driver.find_element_by_xpath('//*[@id="oa_main"]')
driver.switch_to.frame(hh)
xiframes = driver.find_element_by_xpath('//*[@id="frmUserList"]')
driver.switch_to.frame(xiframes)
driver.find_element_by_xpath('//*[@id="userName"]').send_keys('text')