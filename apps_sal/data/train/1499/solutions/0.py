from sys import stdin,stdout
import math,bisect
from collections import Counter,deque,defaultdict
L=lambda:list(map(int, stdin.readline().strip().split()))
M=lambda:list(map(int, stdin.readline().strip().split()))
I=lambda:int(stdin.readline().strip())
S=lambda:stdin.readline().strip()
C=lambda:stdin.readline().strip().split()
def pr(a):return(" ".join(list(map(str,a))))
#_________________________________________________#


def solve():
 n, m = M()
 a = []
 for i in range(n):
  a += [L()]
 s = S()
 p, q = M()
 ans = [[0,0] for i in range(n+m)]
 for i in range(n):
  for j in range(m):
   if a[i][j]==0:
    ans[i+j][0]+=1
   else:
    ans[i+j][1]+=1
 c = 0
 for i in range(n+m-1):
  A,B,C,D = 0,0,0,0
  if s[i]=='0':
   A = ans[i][1]*p
   B = q + ans[i][0]*p
   c+=min(A,B)
  else:
   C = ans[i][0]*p
   D = q + ans[i][1]*p
   c+=min(C,D)
 print(c)
for _ in range(I()):
 solve()

