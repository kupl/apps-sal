for _ in range(int(input())):
	n = int(input())
	main = 2
	count = 2
	for i in range(n):
		count = main
		for j in range(n):
			print(count, end="")
			count += 1
		main += 1
		print()
	
		
