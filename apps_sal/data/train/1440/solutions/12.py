for _ in range(int(input())):
 n=int(input())
 a=list(map(int,input().split()))
 d=a[0]%a[1]
 for i in range(2,n):
  d=d%a[i]
 print(d)
