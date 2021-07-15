t=int(input())
mod = 1000000007
for i in range(t):
	n, m = map(int, input().split())
	print("Case {:d}:".format(i+1))
	for j in range(m):
		arr = input()
		l = len(arr)
		if l > n:
			print(0)
		else:
			prod = pow(26, n-l, mod)*(n-l+1)
			print(prod%mod)
			
