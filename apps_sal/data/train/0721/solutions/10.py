mod, i=1000000007, 280000002
for _ in range (int(input())):
	n=int(input())
	t=((2*26*(pow(26,n//2,mod)-1)*i)%mod+(n&1)*pow(26,(n+1)//2,mod))%mod
	print(t)

