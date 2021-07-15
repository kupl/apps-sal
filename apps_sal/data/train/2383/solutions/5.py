q = int(input())
for i in range(q):
	a,b = map(int,input().split())
	if a > b:
		a,b = b,a
	if 2*a<=b:
		bok = b
	else:
		bok = 2*a
	print(bok**2)
