T=int(input())
for i in range(T):
 L=list(map(int,input().split()))
 P=L[-1]
 L.remove(P)
 for j in range(len(L)):
  L[j]=L[j]*P
 S=sum(L)
 if S>120:
  print("Yes")
 else:
  print("No")

