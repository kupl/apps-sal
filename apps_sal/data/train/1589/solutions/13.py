for _  in range(int(input())):
	a=list(map(int,input().split()))
	a.remove(-1)
	b=[]
	d=[]
	c=0
	s=0
	for i in range(len(a)):
		if a[i]>30:
			c+=1
		if a[i]%2==0:
			b.append(a[i])
			d.append(i+1)
	for j in range(len(b)):
		s+=b[j]*d[j]
	r=s/sum(d)
	print('{} {:.2f}'.format(c,r))
