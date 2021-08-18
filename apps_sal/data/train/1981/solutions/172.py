import math
import bisect
from typing import List
from collections import defaultdict


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        r_arr = [0] * len(nums)
        MOD = 10 ** 9 + 7
        for r in requests:
            r_arr[r[0]] += 1
            if r[1] < len(r_arr) - 1:
                r_arr[r[1] + 1] -= 1

        idxes = defaultdict(lambda: [])
        idxes[r_arr[0]].append(0)
        for r in range(1, len(r_arr)):
            r_arr[r] += r_arr[r - 1]
            idxes[r_arr[r]].append(r)

        ks = list(idxes.keys())
        ks.sort(reverse=True)

        res_arr = [0] * len(nums)
        nums.sort(reverse=True)
        for k in ks:
            for ele in idxes[k]:
                res_arr[ele] = nums.pop(0)

        res = 0
        for i in range(len(res_arr)):
            res += (res_arr[i] * r_arr[i]) % MOD
        return res % MOD
