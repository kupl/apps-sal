from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")


def main():
    n, l = map(int, input().split())
    ss = [input()[:-1] for _ in range(n)] + ["$"]
    ss.sort()

    cnt_tree = defaultdict(int)
    cnt_tree[l] = 2
    for s0, s1 in zip(ss, ss[1:]):
        for depth, (c0, c1) in enumerate(zip(s0, s1)):
            if c0 == c1:
                continue
            cnt_tree[l - depth] -= 1
            for lv in range(l - depth - 1, l - len(s1), -1):
                cnt_tree[lv] += 1
            break

    sum_xor = 0
    for lv, cnt in cnt_tree.items():
        if cnt % 2 == 0:
            continue
        sum_xor ^= lv & -lv

    if sum_xor:
        print("Alice")
    else:
        print("Bob")


main()
