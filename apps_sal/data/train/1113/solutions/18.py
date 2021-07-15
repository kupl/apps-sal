n=int(input())
for i in range(1,n+1):
	k=int(input())
	t=[0]*10001
	s=input().split()
	for j in range(0,k):
		l=int(s[j])
		t[l]+=1
	max=0
	for j in t:
		if j > max:
			max = j
	for l,j in enumerate(t):
		if j == max:
			print(str(l) + " " + str(j))
			break


