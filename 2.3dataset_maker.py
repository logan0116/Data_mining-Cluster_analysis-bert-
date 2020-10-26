import csv
import os
import json
import re

if __name__ == '__main__':
    csv_read_file_path = '词向量预处理数据_1/test_2_span.csv'

    csv_read = csv.reader(open(csv_read_file_path, 'r', encoding='UTF-8'))
    data_set = []
    for each_line in csv_read:
        inf = each_line[1]
        inf = '[CLS] ' + inf + ' [SEP]'
        print(inf)
        data_set.append(inf)

    print(len(data_set))
    json_write_file_path = '词向量预处理数据_2/test.json'
    json_write_file = open(json_write_file_path, 'w', encoding="UTF-8")
    json.dump(data_set, json_write_file)
