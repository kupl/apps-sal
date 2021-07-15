# cook your dish here
t=int(input())
for x in range(t):
 m=0
 
 l=[int(i) for i in input().split()]
 for i in range(0,1<<4):
  ans=0
  for j in range(0,4):
   f=1<<j
   if i&f!=0:
    ans=ans+l[j]
    if ans==0:
     m=1
     print("Yes")
     break
  if m==1:
   break
 else:
  print("No")
   

