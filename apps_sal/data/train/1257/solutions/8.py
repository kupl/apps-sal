#!/usr/bin/env python

def fact(N):
 P = 1
 for n in range(2, N + 1):
  P *= n
 return P

T = int(input())
for t in range(T):
 N = int(input())
 print(fact(N))


