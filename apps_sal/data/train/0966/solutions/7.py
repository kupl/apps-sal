# cook your dish here
for _ in range(int(input())):
 n,u,d=list(map(int,input().split()))
 l=list(map(int,input().split()))
 p=0
 c=0
 for i in range(1,n):
  if l[i]>=l[i-1]:
   if l[i]-l[i-1]<=u:
    c+=1
   else:
    break
  else:
   if l[i-1]-l[i]<=d:
    c+=1
   elif p==0:
    c+=1
    p=1
   else:
    break
 print(c+1)
  
    
  

