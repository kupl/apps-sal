import math
for _ in range(int(input())):
     n,m,k = map(int,input().split())
     a = list(map(int,input().split()))
     total = 0
     for v in a:
          if(v%m == 0):
               y = m
          else:
               y = v%m
          x = math.ceil(v/m)
          total += x*(n+1-x)*y*(m+1-y)
     ans = total / (n * (n+1) * m * (m+1) // 4)
     print("%.11f"%(ans))
