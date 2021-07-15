import math
T=int(input())
for i in range(T):
	n=int(input())
	l=[int(x) for x in input().split()]
	s=math.ceil(n/min(l))
	print(s)
