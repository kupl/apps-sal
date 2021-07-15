from collections import Counter
for _ in range(int(input())):
 
 n = int(input())
 a = sorted(map(int,input().split()))
 b = sorted(map(int,input().split()))
 x=Counter(a)
 y=Counter(b)
 z=x+y
 l=[]
 q=min(a[0],b[0])
 for k in z.keys():
  
  if z[k]%2==1:
   print(-1)
   break
  else:
   l.extend([k]*(abs(x[k]-y[k])//2))
   
 else:
  l.sort()
  ans=0
  
  if l==[]:
   print(0)
  else:
   for i in range((len(l)//2)):
    
    ans+=min(l[i],2*q)
    
   print(ans)
