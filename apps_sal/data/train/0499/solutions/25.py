class Solution:

    def minNumberOperations(self, target: List[int]) -> int:
        res = pre = 0
        for a in target:
            res += max(a - pre, 0)
            pre = a
        return res
