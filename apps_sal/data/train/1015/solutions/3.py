for _ in range(int(input())):
	n = int(input())
	count = 2
	for i in range(n):
		for j in range(n):
			print(count, end="")
			count += 2
		print()
	
