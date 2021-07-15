from math import factorial
k,s,res=int(input()),int(input()),1
for i in range(1,k):
	x=int(input())
	s+=x
	res=(res*factorial(s-1)//factorial(x-1)//factorial(s-x))%1000000007
print(res)
