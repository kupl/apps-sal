t=int(input())
for _ in range(t):
 n=int(input())
 list1=list(map(int,input().strip().split()))
 
 x=max(list1)
 map1=dict()
 ans=1
 ans1=[]
 ans2=[]
 for val in list1:
  if val not in map1:
   map1[val]=1
   ans1.append(val) 
  else:
   if map1[val]==1 and val!=x:
    map1[val]+=1
    ans2.append(val)
   else:
    ans=0
    break
 
 if ans:
  print("YES")
  ans1.sort()
  ans2.sort()
  
  for i in range(len(ans1)):
   print(ans1[i],end=" ")
  for i in range(len(ans2)-1,0-1,-1):
   print(ans2[i],end=" ")
  
  print()
 
 else:
  print("NO")
  
 
 
 
 
 
 
 
 
 
 


