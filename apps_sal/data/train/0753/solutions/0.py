for t in range(int(input())):
	l1=list(map(int,input().split()))
	l2=list(map(int,input().split()))
	l3=list(map(int,input().split()))
	max=0
	g=l1[0]+l2[0]+l3[0]
	y=l1[1]+l2[1]+l3[1]
	r=l1[2]+l2[2]+l3[2]
	if g%2==0:
		g-=1
	if y%2==0:
		y-=1
	if r%2==0:
		r-=1
	if max<g:
		max=g
	if max<r:
		max=r
	if max<y:
		max=y
	m=l1[0]+l1[1]+l1[2]
	o=l2[0]+l2[1]+l2[2]
	p=l3[0]+l3[1]+l3[2]
	if m%2==0:
		m-=1
	if o%2==0:
		o-=1
	if p%2==0:
		p-=1
	if max<m:
		max=m
	if max<o:
		max=o
	if max<p:
		max=p

	print(max)

