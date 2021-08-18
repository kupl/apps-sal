
"""

created by shuangquan.huang at 1/15/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class ListNode:
    def __init__(self, v, d, p, index):
        self.v = v
        self.d = d
        self.p = p
        self.index = index
        self.left = None
        self.right = None


def list2a(head):
    a = []
    h = head
    while h:
        a.append(h.p)
        h = h.right
    return a


def solve(N, A):
    head = ListNode(A[0][0], A[0][1], A[0][2], 1)
    h = head
    for i in range(1, N):
        v, d, p = A[i]
        node = ListNode(v, d, p, i + 1)
        h.right = node
        node.left = h
        h = node

    ans = []
    h = head
    while h:
        ans.append(h.index)
        nh = h.right
        cry = h.v
        while nh and cry > 0:
            nh.p -= cry
            cry -= 1
            nh = nh.right

        ch = h
        nh = h.right
        while nh:
            if nh.p < 0:
                cry = nh.d
                dh = nh.right
                while dh:
                    dh.p -= cry
                    dh = dh.right

                ch.right = nh.right
                if nh.right:
                    nh.right.left = ch

            else:
                ch = nh
            nh = nh.right
        h = h.right

    print(len(ans))
    print(' '.join(map(str, ans)))


N = int(input())
A = []
for i in range(N):
    v, d, p = list(map(int, input().split()))
    A.append([v, d, p])

solve(N, A)
