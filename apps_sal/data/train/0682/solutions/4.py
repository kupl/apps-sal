# your code goes here
import math
n=int(input())
arr=list(map(int,input().split()))
lst=[0]*(n+1)
for i in range(0,n):
	lst[arr[i]]=i+1
i=1
while i<=n:
	if lst[i]!=i:
		break
	i+=1
if i==n+1:
	print('0 0')
else:
	j=lst[i]
	k=j+1
	l=i
	r=j
	while i<=j:
		if lst[i]!=j or lst[j]!=i:
			break
		i+=1
		j-=1
	if i<=j:
		print('0 0')
	else:
		while k<=n:
			if lst[k]!=k:
				break
			k+=1
		if k<=n:
			print('0 0')
		else:
			print(l,' ',r)
		

