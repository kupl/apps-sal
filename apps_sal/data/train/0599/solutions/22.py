class node:
 def __init__(self, size, elements):
  self.size = size
  self.elements = elements


def solve(ele, s):
 m = max(ele)
 i, j = 0, 0
 flag = True
 for k in range(s):
  if ele[k] == m:
   j = k
   if flag:
    flag = False
    i = k
 if i == j:
  return s//2
 elif (j-i) >= s//2:
  return 0
 else:
  i, j = s//2, j + s//2 - i
  return s-j


def __starting_point():
 t = int(input())
 inputs = []
 for i in range(t):
  inputs.append(node(int(input()), list(map(int, input().split()))))
 for i in inputs:
  print(solve(i.elements, i.size))

__starting_point()
