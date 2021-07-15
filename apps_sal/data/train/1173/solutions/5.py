t=int(input())
for _ in range(t):
 n=int(input())
 l=list(map(int,input().split()))
 ans=0
 
 
 m=[0]*n
 for i in range(n):
  if i==0:
   m[i]=l[i]
  else:
   m[i]=m[i-1]^l[i]
 d={}
 c=0
 for i in l:
  c=c^i
 
 for i in range(n-1,-1,-1):
  try:
   x=d[l[i]^c]
   ans+=x[0]-x[1]*i
  except:
   pass
  try:
   d[m[i]]=[d[m[i]][0]+i,d[m[i]][1]+1]
  except:
   d[m[i]]=[i,1]
  c=c^l[i]
 print(ans)

