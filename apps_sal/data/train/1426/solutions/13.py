t=int(input())
while(t>0):
 n,k=list(map(int,input().split()))
 l=[0]+list(map(int,input().split()))
 s=0
 m=[]
 for i in range(n):
  d,f,b=list(map(int,input().split()))
  if(l[d]>0):
   l[d]-=1
   s+=f
   m.append(d)
  else:
   s+=b
   m.append(0)
 c=0
 for i in range(n):
  if(m[i]==0):
   for j in range(c,k+1):
    if(l[j]>0):
     c=j
     m[i]=j
     l[j]-=1
     break
 print(s) 
 print(*m)
 t-=1

