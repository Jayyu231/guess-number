# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了!"
# 猜錯的話 要告訴他 比答案大/小

import random
r = random.randint(1,100)
c = 0
while True :
	user_input = input('Guess a number')
	c += 1 #c = c + 1
	user_input = int(user_input)
	if user_input == r :
		print('終於猜對了!')
		break
	elif user_input < r :
		print('答案比較大')
	elif user_input > r :
		print('答案比較小')
