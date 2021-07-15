# cook your dish here
for _ in range(int(input())):
 n,k=list(map(int,input().split()))
 s=input()
 l=u=0
 for i in s:
  if(i.islower()):
   l+=1
  else:
   u+=1
 if(l<=k and u<=k):
  print("both")
 elif(u>k and l<=k):
  print("brother")
 elif(l>k and u<=k):
  print("chef")
 else:
  print("none")

