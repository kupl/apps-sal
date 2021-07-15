# cook your dish here
for _ in range(int(input())):
 n,m=[int(x) for x in input().split()]
 a=[int(x) for x in input().split()]
 a.sort()
 f=1
 m=10**9+7
 d=[0 for i in range(n)]
 for i in a:
  d[i]+=1
 for i in range(2,n):
  f*=d[i-1]**(d[i])
  f%=m
 print(f)
