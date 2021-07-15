 #!/usr/bin/env python
"""Python Version:3.7.1"""
#start
P, S = list(map(int, input().split()))
COUNT = [0] * 101010
A = []
B = []
for i in range(P):
 A = list(map(int, input().split()))
 B = list(map(int, input().split()))
 A, B = list(zip(*sorted(zip(A, B))))
 for X in range(S-1):
  if B[X] > B[X+1]:
   COUNT[i] += 1
for i in range(31):
 for j in range(P):
  if COUNT[j] == i:
   print(j+1)
#end

