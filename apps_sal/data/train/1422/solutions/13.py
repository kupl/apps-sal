#!/usr/bin/env python

def process(N, S):
 C = 0
 for i in range(1, N + 1):
  if S[i-1] or S[i] or S[i+1]:
   C += 1
 return N - C

def main():
 T = int(input().strip())
 for t in range(T):
  N = int(input().strip())
  S = [0] + list(map(int, input().strip())) + [0]
  print(process(N, S))

main()


