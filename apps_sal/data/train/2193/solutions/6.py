n=int(input())
l=list(map(int,input().strip().split()))
count=1
r=sum(l)
for i in range(n-1):
	l=list(map(int,input().strip().split()))
	r1=sum(l)
	if r1>r:
		count=count+1
print (count)

