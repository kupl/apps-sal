class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        cur = 0
        i = 1
        while cur < k:
            if arr.count(i) == 0:
                cur = cur + 1
                res = i
            i = i + 1
        return res
