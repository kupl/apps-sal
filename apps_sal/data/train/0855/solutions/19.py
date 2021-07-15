t= int(input())
for i in range(t): 
	s= input()
	sl= len(s)
	for j in range(sl-1,-1,-1):
		print(s[j],end="")
