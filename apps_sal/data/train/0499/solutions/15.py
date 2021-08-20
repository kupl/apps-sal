class Solution:

    def minNumberOperations(self, target: List[int]) -> int:
        (prev, ans) = (None, 0)
        for t in target:
            if prev is not None:
                if t >= prev:
                    ans += t - prev
            else:
                ans += t
            prev = t
        return ans
