from collections import defaultdict as dd
from collections import deque
import bisect
import heapq


def ri():
    return int(input())


def rl():
    return list(map(int, input().split()))


def solve():
    n, k = rl()
    S = input()
    zero_blocks = dd(int)
    cost_all_zeros = 0
    rem = 0
    for i, c in enumerate(S):
        if c == '1':
            cost_all_zeros += 1
            zero_blocks[rem] += 1
        rem += 1
        if rem == k:
            rem = 0

    global_best = n
    for offset in range(k):
        zero_others = cost_all_zeros - zero_blocks[offset]

        pre, mid, post = 0, n, n
        for i in range(offset, n, k):
            if S[i] == '1':
                new_pre = pre + 1
                new_mid = min(mid, pre)
                new_post = min(post + 1, mid + 1)
            else:
                new_pre = pre
                new_mid = min(mid + 1, pre + 1)
                new_post = min(post, mid)
            pre, mid, post = new_pre, new_mid, new_post
        best = min(pre, mid, post)

        global_best = min(global_best, best + zero_others)

    print(global_best)


mode = 'T'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
