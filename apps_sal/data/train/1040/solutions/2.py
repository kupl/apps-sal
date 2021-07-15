def precumpute(s, n):
 a = [0 for i in range(n)]
 b = [0 for i in range(n)]
 if n < 3:
  return b
 for i in range(n - 3, -1, -1):
  if s[i] == s[i + 1] or s[i + 1] == s[i + 2] or s[i] == s[i + 2]:
   a[i] = 1
 prev = -1
 for i in range(n - 1, -1, -1):
  if a[i] == 1:
   prev = i
  b[i] = prev
 return b


def solve(b, n, l, r):
 if n < 3:
  print("NO")
  return
 x = b[l]
 if x>=l and x <= r-2:
  print("YES")
 else:
  print("NO")


def read():
 t = int(input())
 for j in range(t):
  n, q = list(map(int, input().strip().split()))
  s = input().strip()
  b = precumpute(s, n)
  for i in range(q):
   l, r = list(map(int, input().strip().split()))
   solve(b, n, l-1, r-1)


read()

