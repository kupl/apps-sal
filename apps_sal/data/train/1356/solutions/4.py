#!/usr/bin/env python

BELL = []
for i in range(1000): BELL.append([0] * 1000)
BELL[0][0] = 1

for r in range(1, 1000):
 BELL[r][0] = BELL[r-1][r-1]
 for c in range(1, r + 1):
  BELL[r][c] = (BELL[r-1][c-1] + BELL[r][c-1]) % 1000000007

def main():
 T = int(input())
 for t in range(T):
  N = int(input())
  print(BELL[N-1][N-1])

main()


