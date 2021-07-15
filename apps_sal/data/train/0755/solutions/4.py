m = int(input())
a = []
for i in range(m):
	a.append(int(input()))
ma = max(a)
x = a.index(ma)
k = max(a[:x]+a[x+1:])
for i in range(2,k):
	flag = 1
	for j in range(m-1):
		if (a[j]%i != a[j+1]%i):
			flag = 0
			break
	if (flag == 1):
		print(i,end = " ")
