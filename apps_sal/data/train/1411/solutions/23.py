# cook your dish here
import sys
import math


def main():
 input = sys.stdin.readline
 t = int(input())

 while t > 0:
  t -= 1
  x, r, a, b = (int(i) for i in input().split())

  circle = 2 * r * math.pi
  total = x * circle

  if a < b:
   a, b = b, a

  time = total / a
  y = b * time
  y = y / circle

  res = math.ceil(x - y) - 1

  print(res)


main()

