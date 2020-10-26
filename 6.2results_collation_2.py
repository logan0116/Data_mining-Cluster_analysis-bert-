import csv
import os

if __name__ == '__main__':
    cluster_path = 'cluster'
    cluster_list = os.listdir(cluster_path)

    for each_cluster_path in cluster_list:
        csv_read = csv.reader(open(os.path.join(cluster_path, each_cluster_path)))
        txt_str = ''
        for each_record in csv_read:
            title = each_record[0][:-1].replace('"', '').replace(',', '')
            txt_str += title + ' '
        word_list = txt_str.split()
        word_dict = dict()
        for each_word in word_list:
            each_word = each_word.lower()
            if each_word not in word_dict:
                word_dict[each_word] = 1
            else:
                word_dict[each_word] += 1
        word_dict_sorted = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)[1:51]
        ket_list = []
        for i in word_dict_sorted:
            ket_list.append(i[0])
        print(ket_list)

