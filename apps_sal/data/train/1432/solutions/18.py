for _ in range(int(input().strip())):
	n = int(input().strip())
	total_ones = 0
	for _ in range(n):
		total_ones += sum(list(map(int, input().strip().split())))
	i = 0
	total_ones -= n
	while total_ones>0:
		i += 1
		total_ones -= 2*(n-i)
	print(i)
