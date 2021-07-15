T=int(input())
for i in range(T):
 N=int(input())
 H=list(map(int,input().split()))[:N]
 if N%2!=0 and H[0]==1 and H[N//2]==max(H) and H[-1]==1:
  for j in range(len(H)-1):
   if abs(H[j+1]-H[j])!=1:
    print("no")
    break
  else:
   print("yes")
 else:
  print("no")

