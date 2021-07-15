
import math
t=int(input())
for t1 in range(0,t):
	n=int(input())
	l=list(map(int,input().split()))
	
	if(n==1):
		print(*l)
	else:
		x=l[0]
		y=l[-1]
		l1=[]
		l2=[]
		for i in range(0,n):
			x=math.gcd(x,l[i])
			l1.append(x)
			if(x==1):
				break
		for j in range(n-1,-1,-1):
			y=math.gcd(y,l[j])
			l2.append(y)
			if(y==1):
				break
		#print(l1,l2)
		print(max(max(l1),max(l2)))
