# cook your dish here
T = int(input())
for i in range(T):
 n,k=list(map(int,input().split(" ")))
 if n//k%k==0:
  print("NO")
 else:
  print("YES")

