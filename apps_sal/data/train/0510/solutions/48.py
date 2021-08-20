import sys
import math
import collections
import bisect
import itertools
import fractions
import copy
import decimal
import queue
sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7


def ni():
    return int(sys.stdin.readline())


def ns():
    return list(map(int, sys.stdin.readline().split()))


def na():
    return list(map(int, sys.stdin.readline().split()))


def main():
    n = ni()
    s = list(input())
    q = ni()
    alphabet_idx = {}
    for i in range(26):
        alphabet_idx[i] = []
    for (i, si) in enumerate(s):
        alphabet_idx[ord(si) - ord('a')].append(i)
    for _ in range(q):
        (qi, a, b) = input().split()
        (qi, a) = (int(qi), int(a))
        if qi == 1:
            a -= 1
            if s[a] == b:
                continue
            current_char = ord(s[a]) - ord('a')
            del_idx = bisect.bisect_left(alphabet_idx[current_char], a)
            del alphabet_idx[current_char][del_idx]
            insert_idx = bisect.bisect_left(alphabet_idx[ord(b) - ord('a')], a)
            alphabet_idx[ord(b) - ord('a')].insert(insert_idx, a)
            s[a] = b
        if qi == 2:
            b = int(b)
            a -= 1
            b -= 1
            ans = 0
            for i in range(26):
                a_idx = bisect.bisect_left(alphabet_idx[i], a)
                if a_idx < len(alphabet_idx[i]):
                    if alphabet_idx[i][a_idx] <= b:
                        ans += 1
            print(ans)


def __starting_point():
    main()


__starting_point()
