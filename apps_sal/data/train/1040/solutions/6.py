# cook your dish here
import sys
from math import ceil, floor
import bisect


def RI(): return [int(x) for x in sys.stdin.readline().split()]
def rw(): return sys.stdin.readline().strip()


for _ in range(int(input())):
    n, q = RI()
    st = input()
    bi = []
    for i in range(len(st) - 2):
        if st[i] == st[i + 1] or st[i] == st[i + 2] or st[i + 1] == st[i + 2]:
            bi.append(i)
    # print(bi)
    for qq in range(q):
        a, b = RI()
        a -= 1
        b -= 1
        pos = bisect.bisect_right(bi, a - 1)
        if pos == len(bi) or bi[pos] + 2 > b:
            print("NO")
        else:
            print("YES")
