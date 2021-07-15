import sys
input = lambda : sys.stdin.readline().rstrip()
read = lambda: list(map(int, input().split()))

def solve():
  x1, y1, x2, y2 = read()
  if x1 == x2:
    print(abs(y1 - y2))
  elif y1 == y2:
    print(abs(x1 - x2))
  else:
    print(abs(y1 - y2) + abs(x1 - x2) + 2)
  

for t in range(int(input())):
  solve()
