t=int(input())
for _ in range(t):
 n=int(input()) 
 a=list(map(int,input().split())) 
 if n == 1:
  print(-1)
  continue
 s = list(set(a))
 if len(s)>2:
  print(-1)
  continue
 if len(s)==1:
  if s[0]==n-1:
   print(0)
  elif s[0]==0:
   print(n)
  else:
   print(-1)
  continue
 x = a.count(max(s))
 y=max(s)
 if(y==a.count(min(s))):
  print(x)
 else:
  print(-1)
 # ans = max(s)
 # print(n-ans)

