class Solution:

    def minNumberOperations(self, target: List[int]) -> int:
        res = pre = 0
        for n in target:
            res += max(n - pre, 0)
            pre = n
        return res
