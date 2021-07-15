# cook your dish here
for _ in range(int(input())):
 r,g,b,m=list(map(int, input().split()))
 l=[]
 for i in range(3):
  l1=list(map(int, input().split()))
  l.append(l1)
   
 for i in range(m+1):
  a=0
  b=0
  for j in range(3):
   m=max(l[j])
   if m>a:
    a=m 
    b=j 
    
  for k in range(len(l[b])):
   l[b][k]=l[b][k]//2
    
 print(a)
