# cook your dish here
for _ in range(int(input())):
 n=int(input())
 if n==1:
  print(1)
  continue
 elif n & (n-1)==0:
  print(-1)
 elif n==3:
  print(*[1,3,2])
 elif n==5:
  print(*[2,3,1,5,4])
 elif n>=6:
  res=[1,3,2,6,4,5]+list(range(7,n+1))
  start=8
  while start<n:
   res[start-1],res[start]=res[start],res[start-1]
   start*=2
  print(*res)
