n, m = map(int, input().split())
l = n
f = 1
s = ((n)*(n+1))//2 - l - f
for _ in range(m):
 k = int(input())
 if 2 <= k <= n-1 or k in [f, l]:
  l, f = f, l
 else:
  l = k
 print(s+l+f)
