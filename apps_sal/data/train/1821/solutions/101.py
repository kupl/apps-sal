import math


class Solution:
    def merge_fn(self, x: List[int], y: List[int]) -> List[int]:
        i, j = 0, 0
        res = []
        while i < len(x) and j < len(y):
            if x[i] < y[j]:
                res.append(x[i])
                i += 1
            else:
                res.append(y[j])
                j += 1
        res += x[i:] + y[j:]
        return res

    def helper_iter(self, nums: List[int]) -> List[int]:
        res = deque([[i] for i in nums])
        while res and len(res) > 1:
            x = res.popleft()
            y = res.popleft() if len(res) else []
            res.append(self.merge_fn(x, y))
        return res[0]

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        res = self.helper_iter(nums)
        return res
