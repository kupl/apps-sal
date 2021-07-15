#!/usr/bin/env python

def main():
 N = int(input())
 C = 0
 for n in range(N):
  S = input().strip()
  Pi = S.split()[-1]
  L = [Pi.count(k) for k in map(str, list(range(10)))]
  if L[8] >= L[5] and L[5] >= L[3] and \
   L[0] == 0 and L[1] == 0 and \
   L[2] == 0 and L[4] == 0 and \
   L[6] == 0 and L[7] == 0 and \
   L[9] == 0: C += 1
 print(C)

main()


