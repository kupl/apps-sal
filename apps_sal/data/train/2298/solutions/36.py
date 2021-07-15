n,t=map(int,input().split())
a=list(map(int,input().split()))
m=10**10
M=0
k=[]
for i in range(n):
	m=min(m,a[i])
	M=a[i]-m
	k.append(M)
o=max(k)
print(k.count(o))
