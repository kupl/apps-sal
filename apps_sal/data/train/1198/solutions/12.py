import math
from collections import defaultdict
n=int(input())
a=[int(i) for i in input().split()]
op=defaultdict(int)
gcd=defaultdict(int)
for i in a:
 gcd[i]=1
while(len(a)!=0):
 newa=[]
 x=a[0]
 for i in a[1:]:
  z=math.gcd(x,i)
  gcd[z]+=1
  newa.append(z)
  x=i
 a=newa
for i in gcd:
 j=i
 while(j<10**6+1):
  op[j]+=gcd[i]
  j+=i
q=int(input())
for _ in range(q):
 print(op[int(input())])

