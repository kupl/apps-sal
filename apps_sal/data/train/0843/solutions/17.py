def check(m,arr):
 s=-1
 for i in arr:
  if i<m:
   s=max(s,i)
 return s

t=int(input())
for _ in range(t):
 n=int(input())
 a=[]
 for i in range(n):
  a.append(list(map(int,input().split())))
 s=max(a[-1])
 m=s
 for i in range(n-2,-1,-1):
  m=check(m,a[i])
  if m!=-1:
   s+=m
  else:
   s=-1
   break
 print(s)
 

