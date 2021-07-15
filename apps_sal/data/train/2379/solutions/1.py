import sys
input = sys.stdin.readline
from collections import deque
t = int(input())
for _ in range(t):
  n = int(input())
  a = input()
  ls = []
  st0 = deque()
  st1 = deque()
  for i in range(n):
    if a[i] == "0":
      if st1:
        x = st1.popleft()
        st0.append(x)
      elif st0:
        x = st0[-1]+1
        st0.append(x)
      else:
        x = 1
        st0.append(x)
    else:
      if st0:
        x = st0.pop()
        st1.appendleft(x)
      elif st1:
        x = st1[-1]+1
        st1.append(x)
      else:
        x = 1
        st1.append(x)
    ls.append(x)
  print(max(ls))
  print(*ls)
