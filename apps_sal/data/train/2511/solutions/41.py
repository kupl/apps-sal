class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        N = len(A) / 2
        for num in A:
            if A.count(num) == N:
                return num
