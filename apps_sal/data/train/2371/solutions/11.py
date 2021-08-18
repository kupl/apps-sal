import os
import sys
def _(): return sys.stdin.readline()
def __(): return sys.stdin.readline().split()


N = 100005
q = int(_())
for id in range(q):
    n = int(_())
    a = list(reversed(list(map(int, __()))))
    ans = 0
    check = 0
    for x in range(1, len(a)):
        if not check and a[x] < a[x - 1]:
            check = 1
        if check and a[x] > a[x - 1]:
            ans = len(a) - x
            break
    print(ans)
