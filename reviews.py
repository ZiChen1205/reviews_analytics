data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 100000 == 0:
			print(len(data))
print('檔案讀取完了,總共',len(data),'筆資料')

sum_data = 0
for d in data:
	sum_data= sum_data + len(d)
print('所有留言的平均長度是',sum_data/len(data),'個字元')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('總共有',len(new),'筆留言小於100個字元')
print(new[0])
print(new[1])