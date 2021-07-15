t=int(input())
for z in range (t):
	n,m,k=list(map(int,input().split()))
	a=[([0]*m) for i in range (n)]
	for i in range (n):
		a[i]=list(map(int,input().split()))

	s2=0

	for i in range (n):
		s3=0
		co=0
		for j in range (0,m):
			if(co==k):
				s3=s3+a[i][j]-a[i][j-k]
			else:
				s3=s3+a[i][j]
				co+=1
			if(s3>s2):
				s2=s3

			
			
		
	s3=0
	s4=0
	for i in range (m):
		s3=0
		co=0
		for j in range (0,n):
			if(co==k):
				s3=s3+a[j][i]-a[j-k][i]
			else:
				s3=s3+a[j][i]
				co+=1
			if(s3>s2):
				s2=s3
			
		
	print(s2)

