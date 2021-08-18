
"""

created by shuangquan.huang at 2/11/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def make_trie(A):
    trie = {}
    for word in A:
        t = trie
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]

    return trie


def game(trie):
    if not trie:
        return False

    return not all([game(t) for k, t in trie.items()])


def can_lose(trie):
    if not trie:
        return True

    return any([not can_lose(t) for k, t in trie.items()])


def solve(N, K, A):
    trie = make_trie(A)
    win = game(trie)

    if not win:
        return False

    if K == 1:
        return True

    if can_lose(trie):
        return True

    return K % 2 == 1


N, K = map(int, input().split())
A = []
for i in range(N):
    s = input()
    A.append(s)

print('First' if solve(N, K, A) else 'Second')
