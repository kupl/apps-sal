n = int(input())
s = 0
minb = float("inf")
for _ in range(n):
  a, b = map(int, input().split())
  if a > b:
    minb = min(b, minb)
  s += a
if minb == float("inf"):
  print(0)
else:
  print(s - minb)
