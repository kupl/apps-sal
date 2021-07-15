t=int(input())
l=[]
for i in range(t):
 n=int(input())
 a=list(map(int,input().split()))
 count=0
 for j in range(n-1):
  if a[j]<=a[j+1]:
   a[j+1]=a[j]
   count+=1
 l.append(n-count)
for i in l:
 print(i)

   
   
 
  
 
 
   
  
   
  
  

