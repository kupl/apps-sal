import sys
input = sys.stdin.readline
N = int(input())
res = 0
f = 1
t = 10 ** 10
for _ in range(N):
  x, y = map(int, input().split())
  if x != y: f = 0
  if x > y:
    t = min(t, y)
  res += y
if f:
  print(0)
  return

print(res - t)
