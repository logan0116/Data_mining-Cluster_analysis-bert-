from sklearn.cluster import KMeans
from sklearn.metrics import calinski_harabasz_score

import numpy as np

if __name__ == '__main__':
    text_matrix = np.load('text_matrix.npy')
    print(text_matrix)
    print(text_matrix.shape)
    # test = np.array([[1, 3], [2, 3], [4, 3], [5, 6]])
    # print(test)
    # print(test.shape)
    for i in range(2, 30):
        # 构建并训练模型
        k_means = KMeans(n_clusters=i, random_state=123).fit(text_matrix)
        score = calinski_harabasz_score(text_matrix, k_means.labels_)
        print('数据聚%d类calinski_harabaz指数为：%f' % (i, score))
