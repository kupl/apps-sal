from sys import stdin, stdout
from math import ceil
import numpy as np
from numpy.linalg import matrix_power


def parity(n):
 return bin(n)[2:].count('1') % 2


def solve():
 for _ in range(int(input())):
  s = set()
  q = int(input())
  p = [0, 0]
  while q:
   q -= 1
   x = int(input())
   if s == set():
    p[parity(x)] += 1
    s.add(x)
   else:
    if x not in s:
     se = set()
     for j in s:
      se.add(j ^ x)
      p[parity(j ^ x)] += 1
     s = s.union(se)
     s.add(x)
     p[parity(x)] += 1
   print(p[0], p[1])


def __starting_point():
 solve()

__starting_point()
