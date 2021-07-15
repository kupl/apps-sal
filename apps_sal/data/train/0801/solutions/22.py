t = int(input())
for _ in range(t):
 n = int(input())
 l1 = list(map(int,input().split()))
 l2 = list(map(int,input().split()))
 
 mp = {}
 for i in l1:
  if i in mp:
   mp[i]+=1
  else:
   mp[i]=1
   
 for i in l2:
  if i in mp:
   mp[i]-=1
  else:
   mp[i]=-1
   
 mini=min(l1)
 l2.append(mini)
 mini = min(l2)
 error=False
 l1 = []
 l2 = []
 for k,v in list(mp.items()):
  if abs(v)%2==1:
   error = True
   
  if v>0:
   v = v//2
   for _ in range(v):
    l1.append(k)
  if v<0:
   v = abs(v)//2
   for _ in range(v):
    l2.append(k)
  
 if error == True or len(l1) != len(l2):
  print(-1)
  continue
 
 ans=0
  
 for i in range(len(l1)):
  ans+=min([2*mini,l1[i],l2[i]])
 print(ans)
  
    
    
    
    

