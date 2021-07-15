from collections import Counter
t=int(input())
for i in range(t):
 k=int(input())
 l=list(map(int,input().split()))
 a=Counter(l)
 b=list(a.keys())
 b.sort()
 for x in b:
  s=str(x)+': '+str(a[x])
  print(s)
