class Solution:

    def repeatedNTimes(self, A: List[int]) -> int:
        B = A.copy()
        for x in A:
            B.remove(x)
            if x in B:
                return x
