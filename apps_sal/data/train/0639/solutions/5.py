# cook your dish here
from collections import Counter


def fib_str(s):
 counts = Counter(s)
 if len(counts) < 3:
  return True
 [x, y, z] = counts.most_common(3)
 if x[1] == y[1] + z[1]:
  return True
 return False

def __starting_point():
 test = int(input())

 for _ in range(test):
  s = input()

  if fib_str(s):
   print("Dynamic")
  else:
   print("Not")
__starting_point()
