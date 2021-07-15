for _ in range(int(input())):
 n=int(input())
 a=list(map(int,input().split()))
 s=a[0]%a[1]
 m=a[1]%a[0]
 d=max(s,m)
 for i in range(2,n):
  if d>a[i]:
   d=a[i]%d
  else:
   d=d%a[i]
 print(d)
