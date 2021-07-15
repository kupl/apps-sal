# # cook your dish here
# import sys
# from sys import stdin, stdout
# for _ in range(int(stdin.readline())):
#     N, Q = map(int, stdin.readline().rstrip().split())
#     Num = list(map(int, stdin.readline().split()))
#     for _ in range(Q):
#         P = int(stdin.readline())
#         x = bin(P).count('1')
#         even = 0
#         for i in range(len(Num)):
#             y = bin(Num[i]).count('1')
#             if x % 2 == 0:
#                 if y % 2 == 0:
#                     even += 1
#             else:
#                 if y % 2 != 0:
#                     even += 1
#         stdout.write(str(even) + " " + str(N-even))

import sys

T = int(sys.stdin.readline())
from collections import defaultdict

ans = []
for _ in range(T):
 n ,q = list(map(int ,sys.stdin.readline().split()))
 x = list(map( int ,sys.stdin.readline().split()))

 
 dic = defaultdict(int)
 
 for ele in x:
  if(bin(ele).count('1') %2 == 0):
   dic['even'] += 1
  else:
   dic['odd'] += 1
  
 for o in range(q):
  l = int(sys.stdin.readline())
  
  
  if(bin(l).count('1') % 2 != 0):
   print(dic['odd'],dic['even'])
  else:
   print(dic['even'],dic['odd'])

