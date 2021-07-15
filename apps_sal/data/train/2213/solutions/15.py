t=int(input())
for nt in range(t):
	a,b,n=map(int,input().split())
	c=a^b
	if n%3==0:
		print (a)
	elif n%3==1:
		print (b)
	else:
		print (c)
