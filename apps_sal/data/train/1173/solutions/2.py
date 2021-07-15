import random, math
from copy import deepcopy as dc
from bisect import bisect_left, bisect_right



# Function to call the actual solution
def solution(li):
 ma = {}
 st = {}
 ma[0] = 1
 st[0] = 1
 s = 0
 c = 0
 for i in range(len(li)):
  s ^= li[i]
  c += (ma.get(s, 0)*(i+1)) - st.get(s, 0)
  ma[s] = ma.get(s, 0) + 1
  st[s] = st.get(s, 0) + i + 2
 return c


# Function to take input
def input_test():
 for _ in range(int(input())):
  n = int(input())
  # a, b = map(int, input().strip().split(" "))
  # a, b, c = map(int, input().strip().split(" "))
  li = list(map(int, input().strip().split(" ")))
  out = solution(li)
  print(out)

# Function to check test my code
def test():
 pass


input_test()
# test()

