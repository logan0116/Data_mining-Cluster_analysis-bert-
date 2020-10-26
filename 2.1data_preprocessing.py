# 增加一个数据的预处理
# 长句拆分

import csv
import nltk
from nltk import sent_tokenize


# from deepsegment import DeepSegment

def not_empty(s):
    return s and s.strip()


def get_mean(length_list):
    return sum(length_list) / len(length_list)


def get_var(length_list):
    length_mean = get_mean(length_list)
    length_sum = 0
    for each_length in length_list:
        length_sum += (each_length - length_mean) ** 2
    return length_sum / len(length_list)


def get_special_char(sentence):
    special_char_list = [',', '.', ';', None]
    max_bit = -1
    max_value = -1
    for i in range(len(special_char_list[:-1])):
        value_now = sentence.count(special_char_list[i])
        if value_now > max_value:
            max_value = value_now
            max_bit = i
    return special_char_list[max_bit]


# 获取统计量
def get_statistics(read_file_path):
    patent_file_path = read_file_path
    csv_read = csv.reader(open(patent_file_path, 'r', encoding='UTF-8'))

    length_list = []

    for each_recode in csv_read:
        length_list.append(len(each_recode[1].split()))
    length_mean = get_mean(length_list)
    length_var = get_var(length_list)
    print(length_mean, length_var)
    return length_mean, length_var


def deal(length_mean, read_file_path, write_file_path):
    patent_file_path = read_file_path
    csv_read = csv.reader(open(patent_file_path, 'r', encoding='UTF-8'))
    csv_write = csv.writer(open(write_file_path, 'w', encoding='UTF-8', newline=''))

    count_1 = 0

    for each_recode in csv_read:
        sentence = each_recode[1]
        other_inf = each_recode[2:]
        if len(sentence.strip()) > int(length_mean):
            # 判断一下是否有逗号和句号
            # 没有的话直接写入
            special_char = get_special_char(sentence)
            if special_char is None:
                csv_write.writerow([count_1, sentence.strip(), 1] + other_inf)
                count_1 += 1
                continue
            # 一个小句子如果太短则需要和之后的句子合并
            # 20201008可能有bug
            sentence_small_list_1 = sentence.split(special_char)
            sentence_small_list_1 = list(filter(not_empty, sentence_small_list_1))
            sentence_small_list_2 = []
            combination = ''
            for each_sentence_smell in sentence_small_list_1:
                if len((combination + ' ' + each_sentence_smell).split()) > int(length_mean / 2):
                    sentence_small_list_2.append(combination + ' ' + each_sentence_smell)
                    combination = ''
                else:
                    combination = combination + ' ' + each_sentence_smell  # 20201008这里多了一个 + 号
            if combination:
                sentence_small_list_2.append(combination)

            for each_sentence_smell in sentence_small_list_2:
                csv_write.writerow([count_1, each_sentence_smell.strip(), 1 / len(sentence_small_list_2)] + other_inf)
                count_1 += 1
        else:
            # 如果句子长度比平均值短
            csv_write.writerow([count_1, sentence.strip(), 1] + other_inf)
            count_1 += 1
    print(count_1)


if __name__ == '__main__':
    read_file_path = '词向量预处理数据_1/yjm_20201023.csv'
    length_mean, length_var = get_statistics(read_file_path)
    write_file_path = '词向量预处理数据_1/yjm_20201023_2.csv'
    deal(length_mean, read_file_path, write_file_path)
