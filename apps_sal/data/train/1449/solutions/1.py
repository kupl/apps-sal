for _ in range(int(input())):
	s = input()
	a = s.split('4')
	sum1 = 0
	for k in a:
		sum1 = sum1 + (len(k)*(len(k)+1))/2
	l = len(s) *(len(s)+1) / 2
	print(l - sum1)
