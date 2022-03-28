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

# 篩選留言長度
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
# 整個for loop走完再print
print('一共有', len(new), '筆留言長度小於100個字母')
print(new[0])

'''
# 篩選有good的留言
good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])
'''

# 進階寫法(list comprehension)，濃縮至一行，第一個d可以放任何想放的東西，像是1
good = [d for d in data if 'good' in d]
print(good[0])

# 若包含bad則放進true，反之為false,bad in d為一運算式
bad = []
for d in data:
    bad.append('bad' in d)
print(bad)


# output =[運算 for 變數 in 清單 篩選條件]
bad = ['bad' in d for d in data]
print(bad)
