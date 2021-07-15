t=int(input())
i=0
while i<t:
	a,b=input().split()
	a=int(a)
	b=int(b)
	Max=a+b
	if a>b:
		Min=a
	else:
		Min=b
	print(Min,Max)
	i+=1
