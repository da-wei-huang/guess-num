import random
r = random.randint(1,100)
count = 0
while True:
	count += 1
	num = input('猜個數字')
	num = int(num)
	if num == r:
		print('你猜對囉')
		print('你已經猜了', count, '次')
		break
	elif num > r:
		print('比答案大,再猜看看')
	elif num < r:
		print('比答案小,再猜看看')
	print('你已經猜了', count, '次')
		