# 找呀找呀找拐点，找到一个好拐点

import xlrd
from sklearn.linear_model import LinearRegression
import numpy as np


def get_r(x, y):
    liner_regression = LinearRegression()
    liner_regression.fit(x, y)
    y_p = liner_regression.predict(x)

    y_mean = sum(y) / len(y)
    sst = sum((y - y_mean) ** 2)
    ssr = sum((y_p - y_mean) ** 2)

    return ssr / sst


# 保证结果是一个凹函数
def check(x_list, y_list):
    if (y_list[1] - y_list[2]) / (y_list[0] - y_list[2]) - (x_list[1] - x_list[2]) / (x_list[0] - x_list[2]) <= 0:
        flag = 1
    else:
        flag = -1
    return flag


if __name__ == '__main__':
    book_read = xlrd.open_workbook('聚类结果.xlsx')
    book_read_sheet = book_read.sheet_by_name('Sheet7')

    x = np.array(book_read_sheet.col_values(0))
    y = np.array(book_read_sheet.col_values(1))

    for i in range(len(x) - 2):
        x_1 = x[i:i + 3]
        y_1 = y[i:i + 3]
        r_1 = get_r(x_1.reshape(-1, 1), y_1.reshape(-1, 1))
        check_value = check(x_1, y_1)
        # print(x_1, x_2)
        print(i + 3, r_1, check_value)
