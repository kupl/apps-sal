for t in range(int(input())):
	n=int(input())
	s=input().strip()
	c=0
	flag=0
	for i in range(n):
		if (s[i]=="A" or s[i]=="E" or s[i]=="I" or s[i]=="O" or s[i]=="U") and (s[i-1]=="A" or s[i-1]=="E" or s[i-1]=="I" or s[i-1]=="O" or s[i-1]=="U") :
			flag=1
	if flag and n!=1:
		print("Yes")
	else:
		print("No")

