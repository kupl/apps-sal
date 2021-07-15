
import sys
import math
import os.path
import random
from queue import deque

sys.setrecursionlimit(10**9)

n, = map(int, input().split())
a = deque(list(map(int, input().split())))

s = 0

for _ in range(n):
	x = a.popleft()
	ix = a.index(x)
	s += ix
	a.remove(x)

print(s)
