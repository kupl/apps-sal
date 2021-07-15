import sys
import math
def II():
	return int(sys.stdin.readline())

def LI():
	return list(map(int, sys.stdin.readline().split()))

def MI():
	return list(map(int, sys.stdin.readline().split()))

def SI():
	return sys.stdin.readline().strip()
t = II()
for q in range(t):
	n = II()
	a = LI()
	b = LI()
	x = min(a)
	y = min(b)
	count = 0
	for i in range(n):
		count+=max(a[i]-x,b[i]-y)
	print(count)

