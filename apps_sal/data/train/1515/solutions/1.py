for _ in range(int(input())):
	s = input()
	res = 0
	cnt = 0
	for c in s:
		if 96 < ord(c) < 123:
			cnt += 1
			res += ord(c)
	res -= 97 * cnt
	res += (ord(s[0])-96) * 100 * cnt
	print(res % 1000000007)
