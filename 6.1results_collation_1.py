from sklearn.cluster import KMeans
from sklearn.metrics import calinski_harabasz_score

import numpy as np
import csv

if __name__ == '__main__':
    cluster_num = 6

    text_matrix = np.load('text_matrix.npy')
    k_means = KMeans(n_clusters=cluster_num, random_state=123).fit(text_matrix)
    score = calinski_harabasz_score(text_matrix, k_means.labels_)
    print('数据聚%d类calinski_harabaz指数为：%f' % (cluster_num, score))
    cluster_list = a = [[] for i in range(cluster_num)]
    csv_read = csv.reader(open('词向量预处理数据_1/test_2_span.csv', 'r', encoding='UTF-8'))
    txt_list = []
    for each_record in csv_read:
        txt_list.append(each_record[1:])

    for i in range(len(k_means.labels_)):
        cluster_list[k_means.labels_[i]].append(txt_list[i])

    for i in range(len(cluster_list)):
        csv_write = csv.writer(open('cluster/cluster_' + str(i) + '.csv', 'w', encoding='UTF-8', newline=''))
        for each_record in cluster_list[i]:
            csv_write.writerow(each_record)
