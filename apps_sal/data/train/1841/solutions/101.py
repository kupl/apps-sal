from collections import defaultdict, deque, Counter
from typing import List
import math
import copy
import random
import numpy as np
import bisect
import inspect
import unittest


def cmp(e1, e2):
    if e1[0] > e2[0] or (e1[0] == e2[0] and e1[1] > e2[1]):
        return 1
    elif e1[0] == e2[0] and e1[1] == e2[1]:
        return 0
    else:
        return -1


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr = sorted(arr)
        i, j = 0, len(arr) - 1
        median = arr[j // 2]
        res = []
        while len(res) < k:
            if abs(arr[j] - median) >= abs(median - arr[i]):
                res.append(arr[j])
                j -= 1
            else:
                res.append(arr[i])
                i += 1
        return res

    def getStrongest1(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        assert(n >= k)
        if k == 0:
            return []
        if k == n:
            return arr

        kth = n - (n - 1) // 2
        median = self.findKthMax(arr, kth, cmp=lambda x, y: x - y)

        new_arr = [(abs(e - median), e) for e in arr]

        kmax = self.findKthMax(new_arr, k, cmp)

        res = []
        t = []
        for x, y in new_arr:
            if cmp((x, y), kmax) > 0:
                res.append(y)
            if cmp((x, y), kmax) == 0:
                t.append(y)
        if len(res) == k:
            return res
        else:
            return res + [t[0]] * (k - len(res))

    def findKthMax(self, l, k, cmp):
        if k > len(l):
            return None
        key = np.random.randint(0, len(l))
        keyv = l[key]

        sl = [i for i in l[:key] + l[key + 1:] if cmp(i, keyv) < 0]
        bl = [i for i in l[:key] + l[key + 1:] if cmp(i, keyv) >= 0]

        if len(bl) == k - 1:
            return keyv
        elif len(bl) >= k:
            return self.findKthMax(bl, k, cmp)
        else:
            return self.findKthMax(sl, k - len(bl) - 1, cmp)


def __starting_point():
    s = Solution()
    arr = [6, -3, 7, 2, 11]
    k = 3
    print((s.getStrongest(arr, k)))


__starting_point()
