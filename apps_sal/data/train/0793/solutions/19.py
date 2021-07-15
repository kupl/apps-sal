import math
def gcda(l):
	num1=l[0] 
	num2=l[1] 
	gcdf=math.gcd(num1,num2) 
	  
	for i in range(2,len(l)): 
	    gcdf=math.gcd(gcdf,l[i]) 
	      
	return(gcdf) 

n,R = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr.append(R)
arr = sorted(arr)
ans = 99999999999999
listo = []
for i in range(n-1):
	listo.append(min(ans,arr[i+1] - arr[i]))

print(gcda(listo))

