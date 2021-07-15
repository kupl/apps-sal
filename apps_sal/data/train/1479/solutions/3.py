# cook your dish here
for _ in range(int(input())):
 n=int(input())
 s=[0]*8 
 for i in range(n):
  p,m=list(map(int,input().split()))
  if p<9 and s[p-1]<m:
   s[p-1]=m 
 print(sum(s))
   
 
  
  
  
  
  
  

