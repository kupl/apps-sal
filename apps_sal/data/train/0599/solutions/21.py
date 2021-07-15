from collections import defaultdict
test=int(input())
for _ in range(test):
 r=int(input())
 s=list(map(int,input().split()))
 m=max(s)
 l=int(r/2)
 step=0
 index=[]
 for i in range(len(s)):
  if s[i]==m:
    index.append(i)
 if len(index)==1:
  print(l)
 else:
  diff=index[-1]-index[0]
  if diff+1 > l:
   print(0)
  else:
   print(l-diff)
