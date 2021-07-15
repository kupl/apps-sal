t=int(input())
m=0
h=[]
for d in range(1,t+1):
	u=input()
	u=u.split(" ")
	a=int(u[0])
	b=int(u[1])
	v=a
	if (b>=a):
		m=a+1
	else:
		m=b+1
	h.append(m)
for i in h:
    print(i)

