import collections
import csv
codes = ['a', 'b', 'c', 'd', 'a']
count = collections.Counter(codes)
count_arr = []
for i in count:
    arr = []
    arr.append(i)
    arr.append(count[i])
    count_arr.append(arr)
with open('./股票基金持仓统计.csv', 'w', newline='') as csvFile:
    writer  = csv.writer(csvFile)
    for row in count_arr:
        writer.writerow(row)