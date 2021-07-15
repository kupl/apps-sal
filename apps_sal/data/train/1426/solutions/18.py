# cook your dish here
for _ in range(int(input())):
 n,m=map(int,input().split())
 l=[0]*(m+1)
 assign=[0]*(n+1)
 s=0
 k=list(map(int,input().split()))
 for i in range(m):
  l[i+1]=k[i]
 for i in range(n):
  d,f,b=map(int,input().split())
  if(l[d]>0):
   l[d]-=1
   s+=f
   assign[i]=d
  else:
   s+=b
 j=0
 while(l[j]==0):
  j+=1
 for i in range(n):
  if(assign[i]==0):
   if(l[j]!=0):
    l[j]-=1
    assign[i]=j
   else:
    while(l[j]==0):
     j+=1
    l[j]-=1
    assign[i]=j
 print(s)
 for i in range(n):
  print(assign[i],end=" ")
 print()
  
