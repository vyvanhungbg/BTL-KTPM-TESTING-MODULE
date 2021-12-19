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
from GenerateTest import  *

from openpyxl import Workbook

driver = webdriver.Chrome( service=Service(ChromeDriverManager().install()))
driver.get("http://localhost:8080/login")

def login(username, password):
    input_username = driver.find_element(By.NAME, "useName")
    input_username.send_keys(username)
    input_password = driver.find_element(By.NAME, "password")
    input_password.send_keys(password)
    button_login_submit = driver.find_element(By.ID, "btn-login-submit")
    button_login_submit.click()
    try:
        mess = driver.find_element(By.ID, "error")  # Không thấy mess thì là đăng nhập thành công
        if(mess):
            raise Exception(mess.text)
    except selenium.common.exceptions.NoSuchElementException:
        print("Đăng nhập thành công")


def input_by_id(name_of_element,value_of_element):
    ans = driver.find_element(By.ID,name_of_element)
    ans.clear()
    ans.send_keys(value_of_element)
    mess = ans.get_attribute("validationMessage")
    if(mess):
        raise Exception(" Lỗi nhập trường "+name_of_element + " Nhập không hợp lệ hoặc không được để trống")

def click_by_id_button(id_button):
    button_login = driver.find_element(By.ID,id_button) # chuyển trang login
    button_login.click()

def transaction(amount_money, number_phone_provider):
    input_number_phone_provider = input_by_id("input-number-phone-provider", number_phone_provider)
    input_amount_money = input_by_id("input-amount-money", amount_money)


    button_submit_transaction = driver.find_element(By.ID, "btn-submit-transaction")
    button_submit_transaction.click()

    h2_get_status_transaction = driver.find_element(By.ID, "span-get-status-transaction")
    print(driver.title + " "+ h2_get_status_transaction.text)
    return h2_get_status_transaction.text




def main():
    #Trang home
    #click_by_id_button("btn-login") # Chuyển trang login
    username = "hung"
    password = "hung123"
    # input pass and use name
    login(username, password)

    #chuyển trang chuyển tiền
    click_by_id_button("btn-transaction")

    #So lan test
    loop = 100

    # nhập input cho form transaction
    amount_money = 123
    number_phone_provider = 3287498;

    #Sinh list test field
    list_phone = test_input_field(number_phone_provider,loop)[0]
    list_amount_money =  test_input_field(number_phone_provider, loop)[1]

    #Sinh list test transaction
    #list_phone = test_transaction(number_phone_provider,loop)[0]
    #list_amount_money = test_transaction(number_phone_provider, loop)[1]

    header = ["STT", "SĐT Nhận", "Số tiền", "Trạng thái"]
    #df = pd.DataFrame(columns= header)
    df = pd.DataFrame(columns = header)
    for i in range(0,loop):
        print("Test : ",i)
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
        new_row = [i + 1, number_phone, money, mess]

        df = pd.DataFrame(numpy.insert(df.values, i, new_row, axis=0))
        print(df)
    # df.to_csv('output1.csv', header = True)
    df = pd.DataFrame(df.values, columns= header)
    df.to_excel('output1.xlsx')
    #driver.delete_all_cookies()
    driver.close()




if __name__== "__main__":
    main()
