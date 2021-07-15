for t in range(int(input())):
 n=int(input())
 store=list(map(int,input().split()))
 count=0
 curr=0
 for i in range(n):
  if store[i]==0:
   if curr>0:
    curr+=1
   else:
    curr=1
  else:
   if curr>count:
    count=curr
   curr=0
 if curr>count:
  count=curr
 if count%2==0:
  print("No")
 else:
  print("Yes")

