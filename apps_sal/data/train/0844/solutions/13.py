#!/usr/bin/env python

def main():
 N, K = list(map(int, input().strip().split()[:2]))
 T = [0] * N
 for k in range(K):
  X = input().strip().split()
  if len(X) == 2:
   T[int(X[1])-1] = 1 - T[int(X[1])-1]
  else:
   T = [0] * N
  print(T.count(1))

main()


