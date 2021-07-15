R, C, N = map(int, input().split())

pts = [tuple(map(int, input().split())) for _ in range(N)]

def on_boundary(x1, y1):
  return (x1 == 0 or x1 == R or y1 == 0 or y1 == C)

def perim_until(x, y):
  if x == 0:
    return y
  if y == C:
    return C + x
  if x == R:
    return R + C + (C - y)
  if y == 0:
    return R + C + C + (R - x)
  return -1

perimpts = []
for i, pt in enumerate(pts):
  x1, y1, x2, y2 = pt
  if on_boundary(x1, y1) and on_boundary(x2, y2):
    per1, per2 = perim_until(x1, y1), perim_until(x2, y2)
    perimpts.append((per1, i))
    perimpts.append((per2, i))

perimpts.sort()
def solve():
  stack = []
  seen = [False for _ in range(N)]
  for ppt in perimpts:
    _, ind = ppt
    if seen[ind]:
      if stack[-1] != ind:
        print("NO")
        return
      stack.pop()
    else:
      seen[ind] = True
      stack.append(ind)
  print("YES")
  
solve()
