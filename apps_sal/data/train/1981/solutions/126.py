from collections import deque


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        counter = [0] * n
        enter = list()
        leave = list()
        for l, r in requests:
            enter.append(l)
            leave.append(r)

        enter.sort()
        leave.sort()

        ei = 0
        li = 0
        en = len(requests)
        cnt = 0
        for i in range(n):
            while ei < en and enter[ei] == i:
                ei += 1
                cnt += 1
            counter[i] = cnt
            while li < en and leave[li] == i:
                li += 1
                cnt -= 1

        vals = []
        for i, cnt in enumerate(counter):
            vals.append([-cnt, i])
        vals.sort()

        res = 0
        nums.sort()
        for i, num in enumerate(nums[::-1]):
            res -= num * vals[i][0]
            res = res % (10**9 + 7)
        return res
