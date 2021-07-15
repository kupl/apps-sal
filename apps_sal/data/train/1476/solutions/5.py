def fact(N):
 c=1
 if N==0:
  return 1
 for i in range(1,N+1):
  c*=i
 return c
from collections import Counter
for _ in range(int(input())):
 s=list(input())
 d=Counter(s)
 p=10**9+7
 m=1
 for v in d.values():
  m*=fact(v)
 print((fact(len(s))//m)%p)
