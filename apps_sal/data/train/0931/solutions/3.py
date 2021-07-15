for _ in range(int(input())):
	n=input()
	a=[int(j) for j in input().split()]
	out=0
	for j in a:
		if j%2==0:
			out+=j
	print(out)
