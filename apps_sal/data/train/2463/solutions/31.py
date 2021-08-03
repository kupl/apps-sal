class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False

        for i in range(len(A) - 1):
            if A[i] >= A[i + 1]:
                break
        for j in range(-1, -len(A), -1):
            if A[j] >= A[j - 1]:
                break
        return i == len(A) + j
