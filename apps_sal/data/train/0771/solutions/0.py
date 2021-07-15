from operator import itemgetter
t=int(input())
for i in range(t):
 n=int(input())
 m,f=list(map(int,input().split()))
 x=list(map(int,input().split()))
 my,fy=0,0
 check=[0]*n
 #print check
 for j in range(n):
  if x[j]>0 and x[j]%m==0 and check[j]==0:
   check[j]=1
   my+=1
 #print check
 for j in range(n):
  if x[j]>0 and x[j]%f==0 and check[j]==0:
   check[j]=1
   fy+=1
 if ((((my+fy)*1.0)/n)*100)>=70:
  print("Yes")
  if my>fy:
   print("Multan")
  elif fy>my:
   print("Fultan")
  else:
   print("Both")
 else:
  print("No") 
 #print check

