import sys
import math
from collections import defaultdict,Counter

input=sys.stdin.readline
def print(x):
    sys.stdout.write(str(x)+"\n")

# sys.stdout=open("CP2/output.txt",'w')
# sys.stdin=open("CP2/input.txt",'r')

# mod=pow(10,9)+7
t=int(input())
for i in range(t):
	n=int(input())
	a=list(map(int,input().split()))
	even=[0]*n
	# odd=[0]*n
	ans=0
	pre=[0]*n
	pre[0]=a[0]
	d={a[0]:0}
	if a[0]%2==0:
		even[0]=1
	for j in range(1,n):
		s=d.get(a[j],-1)
		if s==-1:
			d[a[j]]=j
		else:
			if a[j]&1:
				if (pre[j-1]-pre[d[a[j]]])&1:
					ans=max(ans,pre[j-1]-pre[d[a[j]]])
			else:
				if (even[j-1]-even[d[a[j]]])%2==0:
					ans=max(ans,pre[j-1]-pre[d[a[j]]])
			d[a[j]]=j
		pre[j]=pre[j-1]+a[j]
		even[j]=even[j-1]
		if a[j]%2==0:
			even[j]+=1
	print(ans)
