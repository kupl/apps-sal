from sys import setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import *
from bisect import *

def read():
  return int(input())
 
def reads():
  return [int(x) for x in input().split()]

R, C, N = reads()

def edge(x, y):
  return x == 0 or x == R or y == 0 or y == C

def flat(x, y):
  assert edge(x, y)
  if y == 0:
    return x
  elif x == R:
    return R + y
  elif y == C:
    return R + C + (R - x)
  else:
    assert x == 0
    return 2 * R + C + (C - y)

ps = []
for i in range(N):
  x1, y1, x2, y2 = reads()
  if edge(x1, y1) and edge(x2, y2):
    ps.append((flat(x1, y1), i))
    ps.append((flat(x2, y2), i))
ps.sort()

stack = []
for _, i in ps:
  if len(stack) > 0 and stack[-1] == i:
    stack.pop()
  else:
    stack.append(i)

print("YES" if len(stack) == 0 else "NO")
