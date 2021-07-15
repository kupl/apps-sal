import sys
import math
n=int(input())
a=sorted(int(x) for x in sys.stdin)
i=(n//2)-1
j=n-1
k=0
while j>((n//2)-1) and i>=0:
    if 2*a[i]<=a[j]:
        j-=1
        k+=1
    i-=1
#print(a)
print(n-k)
