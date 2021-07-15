import sys
import math

def solution():
 T = int(input().strip())
 for _ in range(T):
  x, k = list(map(float, input().strip().split(' ')))
  original_x = x
  if k == 1:
   a = [float(input().strip())]
   b = [float(input().strip())]
  else:
   a = list(map(float, input().strip().split(' ')))
   b = list(map(float, input().strip().split(' ')))
  for i in range(int(k)):
   x = x + (a[i]/b[i])*(x)
  percentage = ((x - original_x) / x)*100
  print("%d"%(int(percentage)))

solution()
