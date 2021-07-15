for _ in range(int(input().strip())):
	n = int(input().strip())
	arr = list(map(int, input().strip().split()))
	c = 0
	for i in arr:
		if i >= n//2:
			c += 1
	print(c)
