class Solution:

    def repeatedNTimes(self, A: List[int]) -> int:
        for (i, a) in enumerate(A):
            if a in A[:i]:
                return a
