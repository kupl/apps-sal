q=int(input())
for _ in range(q):
	s=input()
	u,r,d,l=0,0,0,0
	for i in s:
		if i=='U':
			u+=1
		elif i=='R':
			r+=1
		elif i=='D':
			d+=1
		else:
			l+=1
	if min(l,r)==0:
		u=min(1,u)
		d=min(1,d)
	if min(u,d)==0:
		l=min(1,l)
		r=min(1,r)
	ans = 'L'*min(l,r)+'U'*min(u,d)+'R'*min(l,r) +'D'*min(u,d)
	print(len(ans))
	print(ans)
	

