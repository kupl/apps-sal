class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        a = sum(A)
        b = sum(set(A))
        n = len(A) // 2
        if a == 0:
            return 0
        c = (a - b) // (n - 1)
        return c
