class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        return (sum(A) - sum(set(A))) // (len(A)// 2 -1)
