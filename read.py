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
print('檔案讀取完畢，總共有', len(data), '筆資料')

# 計算每筆留言平均長度
sum_len = 0
for d in data:
    sum_len = sum_len + len(d)

print('留言的平均長度為', sum_len/len(data))
