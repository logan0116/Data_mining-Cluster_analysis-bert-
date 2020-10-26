import csv
import os

if __name__ == '__main__':
    cluster_path = 'cluster'
    cluster_list = os.listdir(cluster_path)

    time_count = [[0 for j in range(16)] for i in range(len(cluster_list))]
    print(time_count)

    for i in range(len(cluster_list)):
        print(cluster_list[i])
        csv_read = csv.reader(open(os.path.join(cluster_path, cluster_list[i])))
        for each_record in csv_read:
            time = int(each_record[2][:4])
            weight = float(each_record[1])
            if 1998 <= time <= 2013:
                time_count[i][time - 1998] += weight

    for time in time_count:
        print(time)
