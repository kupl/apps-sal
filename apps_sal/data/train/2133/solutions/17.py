a=int(input())
q,w,e,r,t,y,u=0,0,0,0,0,0,0
for i in range(a):
	b=input()
	q+=int(b[0])
	w+=int(b[1])
	e+=int(b[2])
	r+=int(b[3])
	t+=int(b[4])
	y+=int(b[5])
	u+=int(b[6])
print(max(q,w,e,r,t,y,u))

