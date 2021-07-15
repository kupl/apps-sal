import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
 n = int(input().strip())
 ls = list(map(int, input().strip().split()))
 ls.sort()
 if abs(ls[-1]-ls[0])>1: print(-1)
 else:
  if len(set(ls))==1:
   if ls[0]==0: print(len(ls))
   elif len(ls)==ls[0]+1: print(0)
   else: print(-1)
  else:
   i = n-1
   cnt = 0
   while ls[i]==ls[n-1]:
    i-=1
    cnt+=1
   passed = n-cnt
   if ls[0]!=passed-1: print(-1)
   else: print(cnt)

