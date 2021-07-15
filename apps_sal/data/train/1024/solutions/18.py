import math
try:
	t=int(input())
	tot=0
	out=[]
	while(t):
		s,n,k,r = map(int,input().split())
		kin = k

		a=[]
		a.append(k)

		for i in range(n-1):
			k = k*r
			a.append(k)
		k = sum(a)
	# 	k = k - kin
	# 	print(k)
		if s>k:
			
			s=s-k
			out.append(f'POSSIBLE {s}')
			tot+=s
		else:
			
			s=k-s
			out.append(f'IMPOSSIBLE {s}')
			tot-=s
		t-=1
	for i in out:
		print(i)
	if tot>0:
		print('POSSIBLE')
	else:
		print('IMPOSSIBLE')

except EOFError as e:
    print(end="")
