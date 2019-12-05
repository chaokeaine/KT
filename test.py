from selenium import webdriver


driver = webdriver.Chrome()
driver.get("http://192.168.1.246:8090/")
driver.maximize_window()


driver.find_element_by_xpath('//*[@id="login_img"]').click()