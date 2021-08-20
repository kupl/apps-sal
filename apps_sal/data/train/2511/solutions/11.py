class Solution:

    def repeatedNTimes(self, A: List[int]) -> int:
        for i in range(len(A)):
            for j in A[:i]:
                if j == A[i]:
                    return j
