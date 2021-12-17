from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://localhost:8080")

button_login = driver.find_element_by_id("btn-login") # chuyển trang login
button_login.click()

# input pass and use name
input_username = driver.find_element_by_name("useName")
input_username.send_keys("hung")
input_password = driver.find_element_by_name("password")
input_password.send_keys("hung1234")
button_login_submit = driver.find_element_by_id("btn-login-submit")
button_login_submit.click()

#chuyển trang chuyển tiền
button_transaction = driver.find_element_by_id("btn-transaction")
button_transaction.click()

# nhập input cho form transaction
amount_money = 123
number_phone_provider = 3287498;

input_number_phone_provider = driver.find_element_by_id("input-number-phone-provider")
input_number_phone_provider.send_keys(number_phone_provider)

input_amount_money = driver.find_element_by_id("input-amount-money")
input_amount_money.send_keys(amount_money)

button_submit_transaction = driver.find_element_by_id("btn-submit-transaction")
button_submit_transaction.click()

h2_get_status_transaction = driver.find_element_by_id("span-get-status-transaction")


print(driver.title + " "+ h2_get_status_transaction.text)
