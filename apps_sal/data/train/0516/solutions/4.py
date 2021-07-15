import sys
import math
from collections import defaultdict

def fout(s, end='\n'): sys.stdout.write(str(s) + end)
def fin(): return sys.stdin.readline().strip()
mod = pow(10, 9)+7
t = int(fin())
while t>0:
    t -= 1
    n, k = map(int, fin().split())
    a = [int(x) for x in fin().split()]
    ans = 0
    for i in range(n):
        c = 0
        for j in range(i):
            if a[i] < a[j]:
                c += 1
        ans += k*(c)
        for j in range(i+1, n):
            if a[j] > a[i]:
                c += 1
        ans += k*(k-1)*(c)//2
    print(ans)


