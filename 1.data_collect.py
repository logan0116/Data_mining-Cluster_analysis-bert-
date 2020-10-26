import xlrd
import os
import csv


def get_title(str0, str1):
    title = ''
    if str0:
        title = str0
    elif str1:
        title = str1
    return title


def get_time(str0, str1):
    time_list = []
    if str0:
        time_list = sorted(str0.split(' | '))
    elif str1:
        time_list = sorted(str1.split(' | '))
    return time_list[0]


def get_holder(str_holder):
    flag = 0  # 无合作
    if ' | ' in str_holder:
        flag = 1
    return flag


if __name__ == '__main__':
    read_book_file_path = '融合样例文件'
    read_book_file_list = os.listdir(read_book_file_path)

    csv_write_file_path = '词向量预处理数据_1'

    csv_write_path = 'yjm_20201023.csv'
    csv_write_file = open(os.path.join(csv_write_file_path, csv_write_path), 'w', encoding='UTF-8', newline='')
    csv_write = csv.writer(csv_write_file)

    title_list = []
    title_count = 0

    for read_book_file in read_book_file_list:

        csv_read = csv.reader(open(os.path.join(read_book_file_path, read_book_file), 'r', encoding='UTF-8'))
        next(csv_read)
        next(csv_read)

        for each_record in csv_read:
            title = get_title(each_record[0], each_record[2])  # 数据title是在第二列
            time = each_record[8]
            if time == '':
                print(666, time)
            holder = get_holder(each_record[6])
            if title not in title_list:
                title_list.append(title)
                csv_write.writerow([title_count, title, time, holder])
                title_count += 1
        print(read_book_file + '_title个数:', title_count)
