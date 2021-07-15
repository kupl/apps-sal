import sys
input = sys.stdin.readline
for _ in range(int(input())):
  ax, ay, bx, by, cx, cy = map(int, input().split())
  x = (ax + bx + cx)
  y = (ay + by + cy)
  if x == 1 and y == 1:
    print(0)
    continue
  if x == 2 and y == 2:
    print(1)
    continue
  if x == y:
    print(abs(x) - abs(x) // 3 + (x < 0))
    continue
  if x < 0:
    x = abs(x)
    x -= x // 3
    x += 1
  else: x -= x // 3
  if y < 0:
    y = abs(y)
    y -= y // 3
    y += 1
  else: y -= y // 3
  print(max(x, y) - 1)
