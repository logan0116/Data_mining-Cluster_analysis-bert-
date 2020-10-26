# 20201006新加 把停用词里面的词语mask掉

import csv
import re


def get_stop_word_list():
    stop_word_list = []
    csv_read = csv.reader(open('stop_word_list.csv', 'r', encoding='UTF-8'))
    for each_record in csv_read:
        stop_word_list.append(each_record[0])
    return stop_word_list


def deal(read_file_path, write_file_path):
    stop_word_list = get_stop_word_list()
    csv_read = csv.reader(open(read_file_path, 'r', encoding='UTF-8'))
    csv_write = csv.writer(open(write_file_path, 'w', encoding='UTF-8', newline=''))
    # 正则表达式
    pattern = re.compile('[a-z^A-Z^ ^\-]')
    for each_record in csv_read:
        sentence = ''.join(pattern.findall(each_record[1]))
        word_list = sentence.split()
        word_list_span = []
        for each_word in word_list:
            each_word_lower = each_word.lower()
            if each_word_lower in stop_word_list:
                word_list_span.append('[MASK]')
            else:
                word_list_span.append(each_word_lower)
        csv_write.writerow(each_record[:1] + [' '.join(word_list_span)] + each_record[2:])
    print('span完成')


if __name__ == '__main__':
    read_file_path = '词向量预处理数据_1/yjm_20201023_2.csv'
    write_file_path = '词向量预处理数据_1/yjm_20201023_2_span.csv'
    deal(read_file_path, write_file_path)
