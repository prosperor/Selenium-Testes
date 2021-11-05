from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

driver = Chrome()
driver.get("https://www.google.com.br/")
driver.find_element_by_name("q").send_keys("Prats" + Keys.ENTER)
driver.maximize_window()

