import sys
T = int(sys.stdin.readline())
for test in range(T):
 N,M = list(map(int,sys.stdin.readline().split(' ')))

 a = N%M
 if(a%2 == 0):
  print("EVEN")
 else:
  print("ODD")

