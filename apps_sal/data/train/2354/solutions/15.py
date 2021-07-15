s=input()
n=int(input())
l=[]
for u in range(n):
	l.append(input())

flag=0
for i in range(n):
	for j in range(n):
		if((l[i]+l[j]).count(s) >=1):
			flag=1
			break
	if(flag):
		break
if(flag):
	print("YES")
else:
	print("NO")
