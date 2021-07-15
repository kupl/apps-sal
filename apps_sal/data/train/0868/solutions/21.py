from collections import Counter
from math import ceil
test=int(input())
for _ in range(test):
 n,k=list(map(int,input().split()))
 a=list(map(int,input().split()))
 total=0
 for i in range(n):
  for j in range(i+1,n+1):
   subarray=a[i:j]
   length=j-i
   c=Counter(subarray)
   m = (k//length) if (k%length==0) else (k//length+1)
   kth=sorted(subarray)[ceil(k/m)-1]
   F=c[kth]
   if F in c:
    total+=1
 print(total)
   
   

