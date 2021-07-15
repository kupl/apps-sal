t=int(input())
i=0
while i<t:
	a,b=input().split()
	a=int(a)
	b=int(b)
	if a==b:
		print("=")
	elif a>b:
		print(">")
	else:
		print("<")
	i+=1
