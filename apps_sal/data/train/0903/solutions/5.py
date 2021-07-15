for _ in range(int(input())):
	x1,y1=list(map(int,input().split()))
	x2,y2=list(map(int,input().split()))	
	m=(y2-(-y1))/(x2-x1)
	y=y2
	x=x2
	c=y-(m*x)

	y=0
	x=(y-c)/m
	print("{:.2f}".format(x))



