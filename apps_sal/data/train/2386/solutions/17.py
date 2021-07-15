n = int(input())
for _ in range(n):
	a = int(input())
	q = list(map(int,input().split()))
	v =  []
	for i in q:
		if i not in v:
			v.append(i)
	print(*v)
