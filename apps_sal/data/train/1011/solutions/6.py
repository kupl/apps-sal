t=int(input())
for _ in range(t):
 n,k=list(map(int,input().split()))
 s=input()
 l,u=0,0
 for i in range(0,n):
  if(s[i].isupper()):
   u+=1 
  else:
   l+=1 
 if(l<=k and u<=k):
  print("both")
 elif(u>k and l<=k):
  print("brother")
 elif(l>k and u<=k):
  print("chef")
 else:
  print("none")

