import sys
def foo(a,b):
 i=a
 c=b
 n=1
 an=1
 if(a-b)<c:
  c=a-b
 while(n<=c):
  an=(an*i)/n
  i-=1
  n+=1
 return an
tc=eval(input())
for i in range(tc):
 a=input().split()
 total=int(a[0])-1
 selection=int(a[1])-1
 friends=int(a[2])-1
 need=int(a[3])
 res=0
 maxi=foo(total,selection)
 if(need>selection): print("0")
 elif(need<(friends-need)):
  for j in range(need):
   if(((selection-j)>=0) and (total-friends)>=(selection-j)):
    res+=(foo(friends,j)*foo(total-friends,selection-j))
  res=(float)(res)/maxi
  print(1.0000000000-res)
 else:
  for j in range(need,friends+1,1):
   if((selection-j)>=0 and (total-friends)>=(selection-j)):
    res+=(foo(friends,j)*foo(total-friends,selection-j))
  res=float(res)/maxi
  print(res)
