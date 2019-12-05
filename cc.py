from time import sleep
from selenium import webdriver

#进入浏览器
driver = webdriver.Chrome()
driver.get("http://192.168.1.246:8090/")
driver.maximize_window()
sleep(2)

#登录页面
driver.find_element_by_xpath('//*[@id="login_img"]').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[3]/td[3]/input').send_keys('systemadmin')
driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[5]/td[3]/input').send_keys('12345678')
sleep(2)
driver.find_element_by_xpath('//*[@id="myForm"]/table/tbody/tr/td/table/tbody/tr[7]/td[3]/a[1]/img').click()
sleep(2)

driver.switch_to.default_content()
frame1 = driver.find_element_by_xpath('//*[@id="oa_left_middle"]')
driver.switch_to.frame(frame1)
driver.find_element_by_xpath('//*[@id="outlooktitle3"]/table/tbody/tr/td')
