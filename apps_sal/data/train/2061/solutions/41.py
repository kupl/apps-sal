import numpy as np
import sys
from sys import stdin

def short(v):
  x=(v[0]+v[2]+v[4])//3*2+(v[0]+v[2]+v[4])%3-1
  y=(v[1]+v[3]+v[5])//3*2+(v[1]+v[3]+v[5])%3-1
  s=0
  M=max(abs(x),abs(y))
  s=s+M
  if(x==y and x*(x-1)!=0):
    s=s+1
  print(s)
  return
  

def main():
  for i in range(t):
    short(c[i])
  return

input = sys.stdin.readline
t=int(input())
c=[list(map(int,input().split())) for _ in range(t)]
main()
