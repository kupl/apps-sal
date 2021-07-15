t=int(input())
for q in range(t):
 n,l,r=map(int,input().split())
 s=[]
 t1=0
 for i in range(n):
  s.append(1<<i) 
 for i in range(l):
  t1=t1+s[i]
  
 for i in range(n-1,r-1,-1):
  s.pop()
 print(t1+min(s)*(n-l),end=' ')
 maxres=sum(s)

 for i in range(n-len(s)):
  maxres+=max(s)
 print(maxres)
 
