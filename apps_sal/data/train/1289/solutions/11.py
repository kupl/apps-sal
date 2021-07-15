import sys

def DFact(n):
 s = 1
 for i in range(3, n + 1, 2):
  s *= i
 return s

T = int(sys.stdin.readline())
for i in range(T):
 N = int(sys.stdin.readline())
 print(DFact(2 * N - 1))

