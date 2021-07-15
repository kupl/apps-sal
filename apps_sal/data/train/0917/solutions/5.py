t=int(input())
for i in range(t):
 l=[]
 mi=99999999999
 n,m=list(map(int,input().split()))
 a=list(map(int,input().split()))
 for j in range(n-1):
  for k in range(j+1,n):
   a1=a[j]
   a2=a[k]
   b1=a1+a2-m
   b2=abs(b1)
   l.append(b2)
   if(mi>b2):
    mi=b2
    
 print(mi,l.count(mi)) 
   

