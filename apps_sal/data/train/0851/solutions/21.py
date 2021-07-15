for _ in range(int(input())):
	n,k = [int(x) for x in input().split()]
	ans = (1 + n*(k-1))/k
	print(ans*2)
