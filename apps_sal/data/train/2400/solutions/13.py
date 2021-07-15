for nt in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	s=list(set(l))
	s.sort()
	if len(s)==1:
		print (1)
		print (*([1]*n))
	elif len(s)==2:
		print (2)
		a=s[0]
		b=s[1]
		ans=[]
		for i in l:
			if i==a:
				ans.append(1)
			else:
				ans.append(2)
		print (*ans)
	else:
		ans=[1]
		for i in range(1,n):
			if i==n-1:
				if l[i]==l[i-1] and l[0]==l[i]:
					ans.append(ans[-1])
				elif l[i]==l[i-1] and l[i]!=l[0]:
					ans.append((ans[0]%2)+1)
				else:
					temp=(ans[-1]%2)+1
					if l[i]==l[0]:
						ans.append(temp)
					else:
						if temp==ans[0]:
							ans.append(3)
						else:
							ans.append(temp)
				continue
			if l[i]==l[i-1]:
				ans.append(ans[-1])
			else:
				ans.append((ans[-1]%2)+1)
		x=(len(set(ans)))
		if x==2:
			print (2)
			print (*ans)
			continue
		find=0
		for i in range(n-1,0,-1):
			if l[i]==l[i-1]:
				index=i
				prev=ans[i-1]
				find=1
				break
		if not find:
			print (3)
			print (*ans)
		else:
			for i in range(index,n):
				ans[i]=(ans[i-1]%2)+1
			print (2)
			print (*ans)
