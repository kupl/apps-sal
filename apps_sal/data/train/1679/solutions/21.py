# cook your dish here
for _ in range(int(input())):
	n,k,x=map(int,input().split())
	lst=list()
	while(len(lst)!=n):
		lst.append(x)
		if(len(lst)==n):
			break
		for i in range(k-1):
			lst.append(0)
			if(len(lst)==n):
				break
		#print(lst)
	print(*lst,end=" ")
	print()
