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
    s = list(S())
    a=[s[0]]
    for i in range(1,len(s)):
        if a and a[-1]==s[i]:
            a.pop()
        else:
            a.append(s[i])
    print(len(a))
    
for _ in range(I()): 
    solve()

