from sys import stdin,stdout
import math,bisect
from datetime import date
from collections import Counter,deque,defaultdict
L=lambda:list(map(int, stdin.readline().strip().split()))
M=lambda:list(map(int, stdin.readline().strip().split()))
I=lambda:int(stdin.readline().strip())
S=lambda:stdin.readline().strip()
C=lambda:stdin.readline().strip().split()
def pr(a):return("".join(list(map(str,a))))
#_________________________________________________#

def solve():
    n = I()
    a = S()
    d=Counter(a)
    ans=0
    for i in d:
        if d[i]%2:
            ans+=1
    print(max(0,ans-1))
    
for _ in range(I()): 
    solve()

