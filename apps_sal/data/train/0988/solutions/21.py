# cook your dish here
T=int(input())
for i in range(T):
 n=int(input())
 a=list(map(int,input().split()))
 #k=a[0]
 
 s=sum(a)*sum(a)
 for j in range(n):
  q=0
  k=a[j]
  for t in range(n):
   q=q+(k^a[t])
   
  s=min(q,s) 
  
 print(s) 
  
  

