for i in range(int(input())):
	s = input()
	res = 0
	mu = (ord(s[0])-96) * 100
	for c in s:
		if 96 < ord(c) < 123:
			res += ord(c) - 97 + mu
			if res > 1000000007:
				res -= 1000000007
	print(res)
