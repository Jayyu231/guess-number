# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了!"
# 猜錯的話 要告訴他 比答案大/小

#延伸功能 一邊猜一邊告知猜了第幾次?
#延伸功能2 讓使用者決定亂數範圍

import random
a = int(input('自訂猜數字最小值'))
b = int(input('自訂猜數字最大值'))
r = random.randint(a,b)
c = 0
while True :
	user_input = input('Guess a number')
	c += 1 #c = c + 1
	user_input = int(user_input)
	if user_input == r :
		print('猜了第', c ,'次')
		print('終於猜對了!')
		break
	elif user_input < r :
		#print('猜了第', c ,'次')
		print('答案比較大')
	elif user_input > r :
		#print('猜了第', c ,'次') 
		print('答案比較小')
	print('這是你猜的第', c ,'次') 