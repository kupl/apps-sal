t = int(input())
while t > 0:
	t -= 1
	m, n = map(int, input().split())
	a = list(map(int,input().strip().split()))[:m]
	if (max(a) - min(a)) < n:
		print("YES")
	else:
		print("NO")
