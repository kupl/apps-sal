t=eval(input())
for x in range (0,t):
	n=eval(input())
	a=[]
	for i in range (0,n):
		a.append(input())
	c=a[n-1][0]
	a[n-1]=a[n-1].replace("Left","Begin")
	a[n-1]=a[n-1].replace("Right","Begin")
	print(a[n-1])
	for i in range (1,n-1):
		if(c=='R'):
			c=a[n-1-i][0]
			a[n-1-i]=a[n-1-i].replace("Right","Left")
		else:
			c=a[n-1-i][0]
			a[n-1-i]=a[n-1-i].replace("Left","Right")
		print(a[n-1-i])
	if(c=='L'):
		a[0]=a[0].replace("Begin","Right")
	else:
		a[0]=a[0].replace("Begin","Left")
	print(a[0])
		

