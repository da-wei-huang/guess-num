import random
start = input('請輸入數字起始值:')
end = input('請輸入數字終止值:')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	count += 1
	num = input('猜個數字')
	num = int(num)
	if num == r:
		print('你猜對囉')
		print('一共猜了', count, '次')
		break
	elif num > r:
		print('比答案大,再猜看看')
	elif num < r:
		print('比答案小,再猜看看')
	print('一共猜了', count, '次')
		