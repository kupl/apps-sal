from math import ceil
for _ in range(int(input())):
	a=list(input())
	b=list(input())
	n=len(a)
	m=len(b)
	a.sort()
	b.sort()
	i=j=c=0
	while(True):
		if ord(a[i])<ord(b[j]):
			i+=1
		elif ord(a[i])>ord(b[j]):
			j+=1
		else:
			c+=1
			i+=1
			j+=1
		if i==n or j==m:
			break
	print(c)
		

