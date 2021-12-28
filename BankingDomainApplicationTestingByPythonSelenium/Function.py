import numpy

from GenerateTest import load_test_form_excel

import pandas as pd

#list = load_test_form_excel('result.xlsx')


#line_error =

def ThongKe():
    data = pd.read_excel('result.xlsx', sheet_name="Sheet1", index_col=0)
    data_test = pd.read_excel('test.xlsx', sheet_name="Sheet1", index_col=0)
    list_error = data[data['Vượt qua'] == 'FAIL']

    #number_of_error = list_error.drop_duplicates(['Thành công'])

    percent_of_error = list_error.shape[0] * 1.0 / data.shape[0] * 100

    print(list_error)
    print(percent_of_error)


    df1 = pd.DataFrame()
    df1 = df1.append(["Test case lỗi "], ignore_index=True)
    df1 = df1.append(list_error,ignore_index=True)

    df1 = df1.append([""], ignore_index=True)
    df1 = df1.append(["Các test case mẫu "], ignore_index=True)

    for i in list_error.index:  # lay các dòng tương ứng từ file test
        df1 = df1.append(data_test.iloc[i], ignore_index=True)
        print(data_test.iloc[i])

    df1 = df1.append([""], ignore_index=True)
    df1 = df1.append(["Phần trăm số test case lỗi"], ignore_index=True)
    df1 = df1.append([percent_of_error], ignore_index=True)

    df1.to_excel('thongke.xlsx', sheet_name='Sheet1')

#ThongKe() # NHỚ BẬT HÀM THỐNG KÊ NÀY LÊM