T = int(input())
for i in range(T):
	N = int(input())
	l = [int(x) for x in input().split()]
	ans = 0
	s = l[-1]
	for j in reversed(l):
		if(j > s): ans += 1
		else: s = j
	print(ans)

