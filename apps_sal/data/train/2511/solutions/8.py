class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        N = len(A) // 2
        return ((sum(A) - sum(set(A))) // (N - 1))
