from itertools import accumulate
import sys

sys.setrecursionlimit(10 ** 6)
def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]


def main():
    s = SI()
    t = SI()
    s = [0] + [x for x in accumulate([1 if c == "A" else 2 for c in s])]
    t = [0] + [x for x in accumulate([1 if c == "A" else 2 for c in t])]
    q = II()
    for _ in range(q):
        a, b, c, d = MI()
        if (s[b] - s[a - 1]) % 3 == (t[d] - t[c - 1]) % 3:
            print("YES")
        else:
            print("NO")


main()
