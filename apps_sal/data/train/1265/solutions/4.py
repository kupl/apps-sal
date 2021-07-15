a=list()
l=list()
c=0
t=eval(input())
for i in range(0,t):
	k=eval(input())
	if(k<=len(a)):
		print(a[k-1])
	else:
		while(len(a)!=k):
			l=list(map(int,str(c)))
			flag=0
			if(l[0]%2==0):
				for j in range(0,len(l)):
					if(l[j]%2!=0):
						flag=1
						break

			else:
				flag=1

			if(flag==0):
				a.append(c)
			x=10**(len(l)-1)
			if(l[0]%2==0):
				c=c+2
			else:
				c=c+x

		print(a[k-1])
