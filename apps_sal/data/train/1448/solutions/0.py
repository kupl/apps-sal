# cook your dish here

t = int(input())

for _ in range(t):
	a,d,k,n,inc = map(int, input().strip().split())

	res = a
	for i in range(1, n):
		if i%k == 0:
			d += inc
		res += d

	print(res)
