for _ in range(int(input())):
 n ,m = map(int,input().split())
 if n==1 or m==1:
  print(max(n,m))
 else:
  print(n+m-1)
