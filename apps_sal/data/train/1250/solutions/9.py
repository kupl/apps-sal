
t=int(input())
mod=10**9+7
inverse=5*(10**8)+4

for i in range(t):
	n=int(input())
	temp1=pow(3,n+2,mod)
	temp2=pow(2,n+3,mod)
	a=(temp1-temp2+1)%mod
	a=(a*inverse)%mod
	
	print(a)	
