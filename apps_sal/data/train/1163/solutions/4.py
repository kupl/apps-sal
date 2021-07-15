#!/usr/bin/env python

def process(t, N, G):
 Improvment = 0
 CurrentMin = G[0]
 CurrentMax = G[0]
 for n in range(1, N):
  if CurrentMax < G[n]:
   CurrentMax = G[n]
   Improvment = max(Improvment, CurrentMax-CurrentMin)
  elif CurrentMin > G[n]:
    CurrentMin = G[n]
    CurrentMax = G[n]
 return Improvment or 'UNFIT'

def main():
 T = int(input())
 for t in range(T):
  N = int(input())
  G = list(map(int, input().strip().split()[:N]))
  print(process(t, N, G))

main()


