for _ in range(int(input())):
 n=int(input())
 m=[]
 for i in range(n):
  m.append(list(map(int,input().split())))
 lo=[0 for i in range(n)]
 up=[0 for i in range(n)]
 t=0
 for i in range(n):
  for j in range(n):
   if i>j:
    lo[i-j]=lo[i-j]+m[i][j]
   elif i<j:
    up[j-i]=up[j-i]+m[i][j]
   else:
    t=t+m[i][j]
 print(max(lo+up+[t]))
