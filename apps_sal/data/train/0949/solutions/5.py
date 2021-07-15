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

m = 2*pow(10,5)+1
def solve():
    n = I()
    a = L()
    b = [-1]*m
    c = [0]*m
    ans = 0
    for i in range(n):
        if b[a[i]]==-1:
            b[a[i]] = i
        elif i-b[a[i]]==1:
            b[a[i]] = i
            c[a[i]]+=1
            ans = max(ans,c[a[i]])
        elif i-b[a[i]]==2:
            b[a[i]] = i
            c[a[i]]+=1
            ans = max(ans,c[a[i]])
        else:
            b[a[i]] = i
            c[a[i]] = 0
    print(ans)
for _ in range(I()):
    solve()

