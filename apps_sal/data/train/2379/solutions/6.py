import sys
import math
mod = 10**9


def solve(test_index):
    n = int(input())
    s = input()
    a, b = [], []
    p = 0
    ans = []
    for c in s:
        if c == '0':
            if len(a) == 0:
                p += 1
                ans.append(p)
                b.append(p)
            else:
                seq = a.pop()
                ans.append(seq)
                b.append(seq)
        else:
            if len(b) == 0:
                p += 1
                ans.append(p)
                a.append(p)
            else:
                seq = b.pop()
                ans.append(seq)
                a.append(seq)
    print(p)
    print(*ans)
    return


if 'PyPy' not in sys.version:
    sys.stdin = open('input.txt', 'r')

sys.setrecursionlimit(100000)
num_tests = 1
num_tests = int(input())
for test in range(1, num_tests + 1):
    solve(test)
