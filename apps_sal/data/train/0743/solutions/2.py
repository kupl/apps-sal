t = int(input())
while(t):
 n,k = list(map(int,input().split()))
 if n%(k*k)==0:
  print("NO")
 else:
  print("YES")
 t-=1

