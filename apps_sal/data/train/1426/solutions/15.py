for _ in range(int(input())):
 n,m=map(int,input().split())
 c=list(map(int,input().split()))
 l=[]
 ans=0
 for z in range(n):
  d,f,b=map(int,input().split())
  l.append([d,f,b])
 v=[0]*len(l)
 res=[0]*n
 a=[]
 for j,i in enumerate(l):
  if(c[i[0]-1]>0):
   c[i[0]-1]-=1 
   ans+=i[1]
   v[j]=1
   res[j]=i[0]
 s=len(l)
 lc=len(c)
 count=0
 for i in range(s):
  if(v[i]==0):
   ans+=l[i][2]
   count+=1 
 k=[]
 for i in range(lc):
  if(c[i]>0):
   while(c[i]>0 and count>0):
    c[i]-=1 
    count-=1 
    k.append(i+1)
 kl=len(res)
 for i in range(kl):
  if(res[i]==0):
   res[i]=k.pop()
 print(ans) 
 for i in res:
  print(i,end=' ')
 print()
