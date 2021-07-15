#!/usr/bin/env python2
# -*- coding: utf-8 -*-

## Codechef May Challenge 2014
## Chef and Strange Matrix

try:
 import psyco
 psyco.full()
except ImportError:
 pass


def main(N, M, P, tab):
 """Evolved solution"""
 # make a dictionnary with rows and cols increased
 dtab = dict()
 for ii, jj in tab:
  i, j = ii-1, jj-1
  if i in dtab:
   dtab[i].append(j)
  else:
   dtab[i] = [j]

 # move along each row
 for i in range(N):
  sol = M-1
  if i in dtab:
   line = sorted(dtab[i])
   # only the first and the last col give points
   sol += line.count(M-1) - line.count(0)
   # check for unsolvable cases
   prev = -1 # don't repeat k
   for k in line:
    if k > prev and k < (M - 1):
     inc_k = line.count(k)
     inc_kp = line.count(k+1)
     if inc_k > (inc_kp + 1):
      sol = -1
      break
     prev = k

  print(sol)


def __starting_point():
 N, M, P = list(map(int, input().split())) # rows, cols, increasing cmds
 tab = [list(map(int, input().split())) for _ in range(P)]
 main(N, M, P, tab)

__starting_point()
