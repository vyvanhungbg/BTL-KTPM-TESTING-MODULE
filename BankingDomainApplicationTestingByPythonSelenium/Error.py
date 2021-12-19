import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import random
import logger
import numpy
from main import login, transaction, input_by_id, click_by_id_button
from GenerateTest import  *

from openpyxl import Workbook

driver = webdriver.Chrome( service=Service(ChromeDriverManager().install()))
driver.get("http://localhost:8080/login")


username = "hung"
password = "hung123"
# input pass and use name
login(username, password)

#chuyển trang chuyển tiền
click_by_id_button("btn-transaction")

#So lan test
loop = 20

# nhập input cho form transaction
amount_money = 123
number_phone_provider = 3287498;

#Sinh list test field
#list_phone = test_input_field(number_phone_provider,loop)[0]
#list_amount_money =  test_input_field(number_phone_provider, loop)[1]

#Sinh list test transaction
list_phone = test_transaction(number_phone_provider,loop)[0]
list_amount_money = test_transaction(number_phone_provider, loop)[1]

header = ["STT", "SĐT Nhận", "Số tiền", "Trạng thái"]
#df = pd.DataFrame(columns= header)
df = pd.DataFrame(columns = header)
for i in range(0,loop):

    mess = ""
    number_phone = random.choice(list_phone)
    money = random.choice(list_amount_money)
    try:
        mess = transaction(money, number_phone)
        click_by_id_button("btn-return") #Quay lai form chuyển tiền
    except Exception as e:
        print(e)
        mess = e
    loop -= 1
    newline = [i + 1, number_phone, amount_money, mess]

df.append(newline, ignore_index=True)
# df.to_csv('output1.csv', header = True)
df.to_excel('output1.xlsx')
driver.delete_all_cookies()
driver.close()