t=int(input())
for i in range(t):
 N=int(input())
 L=[0]*N
 if N%2==1:
  print("YES")
  for i in range(0,N):
   for k in range(1,int((N+1)/2)):
    L[(i+k)%N]=1
   for m in L:
    print(m,sep="",end="")
   print("")
   L=[0]*N
 else:
  print("NO")





