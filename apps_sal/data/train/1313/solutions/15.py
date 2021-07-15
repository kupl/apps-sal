from functools import reduce
from math import sqrt
from math import gcd
for i in range(int(input())):
	n = int(input())
	li= list((int(i) for i in input().split()))
	a  = reduce(lambda a,b:gcd(a,b),li)
	if a==1:
		print(-1)
	else:
		for i in range(2,int(sqrt(a))+1):
			if a%i==0:
				print(i)
				break
		else:
			print(a)
