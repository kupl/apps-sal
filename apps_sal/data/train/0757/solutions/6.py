# your code goes here
t = int(input())
for j in range(t):
	vow = ['a','e','i','o','u']
	n = int(input())
	s = input().lower()
	ctr=0
	if(n==1):
		if s[0] in vow:
			ctr = 0
	else:
		ctr=0
		for i in range(n-1):
			if s[i] in vow and s[i+1] in vow:
				ctr = 1
				break
		
		if s[0] in vow and s[n-1]in vow:
			ctr = 1
	
	if ctr==0:
		print("No")
	else:
		print('Yes')
