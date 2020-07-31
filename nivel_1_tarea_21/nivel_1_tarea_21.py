x = 0.375
num = int(x*10000)
den = int(10000)
stop = 0
while stop != 1:
	if (num % 7 == 0 and den % 7 == 0):
		num = num / 7
		den = den / 7
	elif (num % 5 == 0 and den % 5 == 0):
		num = num / 5
		den = den / 5
	elif (num % 3 == 0 and den % 3 == 0):
		num = num / 3
		den = den / 3
	elif (num % 2 == 0 and den % 2 == 0):
		num = num / 2
		den = den / 2
	else:
		stop = 1
		print(num,den,sep='/')
		print('fracción irreducible')


