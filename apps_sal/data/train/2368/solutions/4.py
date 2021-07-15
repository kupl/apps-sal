import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	m1 = min(a)
	m2 = min(b)
	ans = 0
	for i in range(n):
		x = a[i]-m1
		y = b[i]-m2
		ans += (min(x,y) + (max(x,y)-min(x,y)))
	print (ans)
