class Solution:

    def validMountainArray(self, A: List[int]) -> bool:
        m = (0, 0)
        for i in range(0, len(A)):
            if A[i] > m[1]:
                m = (i, A[i])
        if m[0] == 0 or m[0] == len(A) - 1:
            return False
        for i in range(0, m[0] - 1):
            if A[i] >= A[i + 1]:
                return False
        for i in range(m[0], len(A) - 1):
            if A[i] <= A[i + 1]:
                return False
        return True
