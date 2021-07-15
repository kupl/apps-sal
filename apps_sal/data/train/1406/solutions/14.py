
import sys

T = int(sys.stdin.readline())
from collections import defaultdict

ans = []
for _ in range(T):
 n ,q = map(int ,sys.stdin.readline().split())
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
