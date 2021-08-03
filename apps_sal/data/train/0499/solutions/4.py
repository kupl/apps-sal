class Solution:
    def minNumberOperations(self, A: List[int]) -> int:
        res = pre = 0
        for a in A:
            res += max(0, a - pre)
            pre = a
        return res
