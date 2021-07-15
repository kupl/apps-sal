T=int(input())
while T:
	a,b,c=map(int,input().split())
	d=c%a
	if d<b:
		i=c-d-a+b
	else:
		i=c-d+b
	print(i)
	T-=1
