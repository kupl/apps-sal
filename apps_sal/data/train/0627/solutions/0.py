import math
p=7+10**9
n,k=list(map(int,input().split()))
c=math.factorial(n+k-1)//((math.factorial(k))*(math.factorial(n-1)))
print(c%p)

