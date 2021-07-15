try:
	t=int(input())
	for _ in range(t):
		n=int(input())
		arr=[]
		for i in range(1,n+1):
			arr.append(i)
		print(*arr)
except:
	pass

