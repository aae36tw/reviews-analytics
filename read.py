'''
#讀取檔案並計算留言數
data = []
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
print(len(data))


# 印出第一、二筆
print(data[0])
print('----------')
print(data[1])

'''

# 每十萬筆印一次讀取數量
data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 100000 == 0:
            print(len(data))

print(len(data))
