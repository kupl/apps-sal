# cook your dish here
for h in range(int(input())):
 n,u,d=map(int,input().split())
 l=list(map(int,input().split()))
 c=1
 x=l[0]
 f=0
 
 for i in range(1,n):
   if l[i]>=x:
    if l[i]-x<=u:
     x=l[i]
     c+=1
    else:
     break
   else:
    if x-l[i]<=d:
     x=l[i]
     c+=1
    elif f==0:
     x=l[i]
     c+=1 
     f=1
    else:
     break
    
 print(c)
