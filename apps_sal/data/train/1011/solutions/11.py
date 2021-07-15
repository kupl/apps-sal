import sys
import math
import bisect
from math import sqrt
def input():    return sys.stdin.readline().strip()
def iinput():   return int(input())
def rinput():   return map(int, sys.stdin.readline().strip().split()) 
def get_list(): return list(map(int, sys.stdin.readline().strip().split())) 
mod = int(1e9)+7

for _ in range(iinput()):
 n, k = rinput()
 s = input()
 cap = low = 0

 for ch in s:
  if ch.upper() == ch:
   cap += 1
  else:
   low += 1

 # print(cap, low)       

 if cap <= k and low <= k:
  print("both")
 elif cap <= k:
  print("chef")
 elif low <= k:
  print("brother")
 else:
  print("none")
