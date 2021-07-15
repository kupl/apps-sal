from sys import stdin
input = stdin.readline
n,m = map(int,input().split())
l = list(map(int,input().split()))
x = sum(l)
if x < n:
	print(-1)
else:
	dasie = True
	for i in range(m):
		if l[i] > n-i:
			dasie = False
	if not dasie:
		print(-1)
	else:
		odp = [1]
		cyk = 1
		while cyk < m:
			x -= l[cyk-1]
			odp.append(max(odp[-1]+1, n+1-x))
			cyk += 1
		print(*odp)
