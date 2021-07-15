import math

T = int(input())

for i in range(T):
  n = int(input())
  #n,k = map(int, input().split())
  a = list(map(int,input().split()))
  b = list(map(int,input().split()))
  #a = input()
  d = False
  
  am = min(a)
  bm = min(b)

  ans = 0
  for i in range(n):
    ans += max(a[i]-am,b[i]-bm)
  print(ans)
