import random

def test_input_field(number_phone_provider, loop):
    special_list = ['', 0, 'string', -1, 1.5]
    random_list = [random.randint(-10000,10000) for i in range(loop)]

    list_amount_money = special_list + random_list
    list_amount_money.append(10000000000)
    special_list.append(number_phone_provider)
    special_list.append(number_phone_provider)
    special_list.append(number_phone_provider)
    list_phone = special_list
    return list_phone, list_amount_money

def test_transaction(number_phone_provider, loop):

    random_list = [random.randint(-10000,10000) for i in range(loop)]

    list_amount_money = random_list
    list_amount_money.append(10000000000)

    list_phone = []
    list_phone.append(number_phone_provider)
    return list_phone, list_amount_money