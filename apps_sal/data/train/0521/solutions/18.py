from math import *

t=int(input())
for i in range(t):
	n=int(input())
	x=[float(y) for y in input().split()]
	x.sort()
	p,q=input().split()
	p=float(p)
	q=float(q)
	ma=0.0
	for ind in range(n//2):
		i=x[ind]
		j=x[n-ind-1]	
		t1=t2=pi/2
		if (i!=p):
			t1=atan(q/abs(i-p))
		if (i>p):
			t1=pi-t1
		if (j!=p):
			t2=atan(q/abs(j-p))
		if (j<p):
			t2=pi-t2
		ma+=(pi-t1-t2)
	print(ma)

