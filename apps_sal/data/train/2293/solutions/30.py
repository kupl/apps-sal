N,r,d=int(input()),0,[[int(s)] for s in input().split()]
for n in range(N):
	B=1<<n
	for i in range(1<<N):
		if i&B:d[i]=sorted(d[i^B]+d[i])[-2:]
for a,b in d[1:]:r=max(r,a+b);print(r)
