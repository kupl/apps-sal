t=int(input())
for tes in range(t):
	n=int(input())
	s=input()
	vow=0
	v=['A','E','I','O','U']
	for i in s:
		if i=='A' or i=='E' or i=='O' or i=='U' or i=='I':
			vow+=1
	if vow<=1:
		print("No")
	else:
		f=0
		if s[0] in v and s[n-1] in v:
			f=1
		for i in range(1,n):
			if s[i] in v and s[i-1] in v:
				f=1
				break
		if f==1:
			print("Yes")
		else:
			print("No")
