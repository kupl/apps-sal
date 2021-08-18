class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:

        step = curr = 0

        for e in sorted(A):

            step += max(curr - e, 0)
            curr = max(curr, e) + 1
        return step
