a=int(input())
for i in range(a):
	b=[int(x) for x in input().split()]
	c=0
	if b[0]>=b[1]:
		print(b[1]+1)
	if b[0]<b[1]:
		print(b[0]+1)
	

