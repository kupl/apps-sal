from collections import deque
t=int(input())

for i in range(t):
 n=int(input())
 N=[i for i in range(1, n+1)]
 w=list(map(int, input().split()))
 max_sweetness=max(w)
 sizes=[]
 cnt=0
 for i in range(n):
  if w[i]!=max_sweetness:
   cnt+= 1 
  else:
   sizes.append(cnt)
   cnt=0
 
 if cnt!=0:
  sizes[0]=(cnt+sizes[0])
 
 res=0
 for i in range(len(sizes)):
  res+=max(sizes[i]-n//2+1, 0)
 
 print(res)
