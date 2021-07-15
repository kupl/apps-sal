'''input
8
3 2
4 2
1 1
3 1
4 7
1 3
7 4
100 100
'''
import math
def solve():
	a,b = map(int,input().split())
	m1 = max(a,b)
	m2 = min(a,b)
	m = max(m1,2*m2)
	print(m*m) 
	return
t = 1
t = int(input())
while t>0:
	t-=1
	solve()
