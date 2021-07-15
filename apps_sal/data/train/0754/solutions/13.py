# cook your dish here
for k in range(int(input())):
	s = input()
	ans = 0
	for p in s:
		if (int(p) % 2) == 0:
			ans = 1
			break
	print(ans)
