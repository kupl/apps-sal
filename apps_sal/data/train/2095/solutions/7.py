n=int(input())
a=list(map(int,input().split()))
par=[]
for i in range(n):
	if a[i]==i+1:
		par.append(i)
v=[False for i in range(n)]
for i in par:
	v[i]=True
ccl=[]
for i in range(n):
	if v[i]:continue
	s=[i]
	v[i]=True
	p=set(s)
	t=True
	while s and t:
		x=s.pop()
		j=a[x]-1
		if j in p:
			ccl.append(j)
			t=False
		else:
			s.append(j)
			p.add(j)
		if v[j]:t=False
		else:v[j]=True
if len(par)==0:
	print(len(ccl))
	c=ccl[0]
	a[c]=c+1
	for i in range(1,len(ccl)):
		a[ccl[i]]=c+1
	print(*a)
else:
	print(len(ccl)+len(par)-1)
	c=par[0]
	for i in range(1,len(par)):
		a[par[i]]=c+1
	for i in range(len(ccl)):
		a[ccl[i]]=c+1
	print(*a)
