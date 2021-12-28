import random
import pandas as pd

def test_input_field(number_phone_provider, loop):
    special_list_money = ['', 0, 'string', -1]
    random_list = [345, 1000]
    bank_list = ['BIDV', 'VIETCOM_BANK', 'VIETTIN_BANK', 'BANK_CKICKEN']
    list_amount_money = special_list_money + random_list
    list_amount_money.append(100000000000)
    list_amount_money.append(10000)

    special_list_phone = ['', -1, 1.5,number_phone_provider]
    return special_list_phone, list_amount_money, bank_list

def test_transaction(number_phone_provider, loop):

    random_list = [random.randint(-10000,10000) for i in range(loop)]

    list_amount_money = random_list
    list_amount_money.append(10000000000)

    list_phone = []
    list_phone.append(number_phone_provider)
    return list_phone, list_amount_money

def load_test_form_excel(file_name):
    df = pd.read_excel(open(file_name,'rb'),sheet_name='Sheet1',dtype=object)
    list = df.values.tolist()

    test = []
    for item in list:
        test.append(item[2:])
    for i in test:
        print(i)
    return test

if __name__== "__main__":
    load_test_form_excel('test.xlsx')