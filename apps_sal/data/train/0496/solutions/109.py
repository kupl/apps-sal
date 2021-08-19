class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        step = 0
        if not A or len(A) == 1:
            return step
        prev = float('-inf')
        nums = sorted(A)
        for e in nums:
            if e <= prev:
                step += prev - e + 1
                prev += 1
            else:
                prev = e
        return step
