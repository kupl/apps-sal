t = int(input())
for _ in range(t):
  n, rep = map(int, input().split())
  a = list(map(int, input().split()))
  ans = 0
  for i in range(len(a)):
    l = 0
    r = 0
    for j in range(i, -1, -1):
      if(a[j] < a[i]):
        l += 1
    for j in range(i, n, 1):
      if(a[j] < a[i]):
        r += 1
    tot = l + r
    lt = tot * (rep - 1) + r
    ans += (rep / 2.0) * (r + lt)
  print(int(ans))
        
  
  
