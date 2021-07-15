for _ in range(int(input())):
	n = int(input())
	num = ""
	val = 1
	for i in range(n):
		num += str(val)
		if val == 1:
			val = 0
		else:
			val = 1
	for i in range(n):
		print(num)
		
	

