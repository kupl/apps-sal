a,b=map(int,input().strip().split())
for j in range(b):
	n=int(input())
	if(n<=a+1 or n>3*a):print(0)
	
	else:
		mi=min(n-a-1,3*a-n+1)
		print(mi)
