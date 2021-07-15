def change(i,j,k):
	nonlocal a
	a[i],a[j],a[k] = a[k],a[i],a[j]

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	arr = a[::]
	b = sorted(a)
	if a==b:
		print (0)
		print ()
		continue
	i = 0
	ans = []
	flag = 0
	while i<n:
		if a[i]==b[i]:
			i += 1
			continue
		ind = a[i:].index(b[i])+i
		# print (ind)
		while a[i]!=b[i]:
			if ind==i+1:
				if ind+1>=len(a):
					flag = 1
					break
				ans.append((i,ind,ind+1))
				change(i,ind,ind+1)
				ans.append((i,ind,ind+1))
				change(i,ind,ind+1)
				break
			else:
				ans.append((ind-2,ind-1,ind))
				change(ind-2,ind-1,ind)
				ind -= 2
		if flag:
			break
		i += 1
		# print (a)
	if flag:
		if len(set(a))==n:
			print (-1)
			continue
		else:
			if a[-3]==a[-1]:
				ans.append((n-3,n-2,n-1))
			else:
				ans = []
				a = arr[::]
				flag2 = 0
				temp = sorted(a,reverse=True)
				for i in range(1,n):
					if temp[i]==temp[i-1]:
						number = temp[i]
						break
				i = 0
				while i<n:
					if a[i]==b[i] and (i==0 or a[i]!=a[i-1] or flag2):
						i += 1
						continue
					elif i!=0 and a[i]==a[i-1]:
						if not flag2 and a[i]==number:
							ans.append((i-1,i,i+1))
							change(i-1,i,i+1)
							ans.append((i-1,i,i+1))
							change(i-1,i,i+1)
							ans.append((i,i+1,i+1))
							change(i,i+1,i+2)
							ans.append((i,i+1,i+2))
							change(i,i+1,i+2)
							flag2 = 1
						i += 1
						continue
					# print (i,a,b)
					ind = a[i:].index(b[i])+i
					# print (ind)
					while a[i]!=b[i]:
						if ind==i+1:
							ans.append((i,ind,ind+1))
							change(i,ind,ind+1)
							ans.append((i,ind,ind+1))
							change(i,ind,ind+1)
							break
						else:
							ans.append((ind-2,ind-1,ind))
							change(ind-2,ind-1,ind)
							ind -= 2
					# print (a,i)
					if i!=0 and a[i]==a[i-1] and flag2==0 and a[i]==number:
						ans.append((i-1,i,i+1))
						change(i-1,i,i+1)
						ans.append((i-1,i,i+1))
						change(i-1,i,i+1)
						ans.append((i,i+1,i+1))
						change(i,i+1,i+2)
						ans.append((i,i+1,i+2))
						change(i,i+1,i+2)
						flag2 = 1
					i += 1
					# print (a)
	
	print (len(ans))
	for i in ans:
		print (i[0]+1,end=" ")
	print ()
