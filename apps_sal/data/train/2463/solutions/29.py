class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] < A[i + 1]:
                i += 1
            if A[j] < A[j - 1]:
                j -= 1
            elif i + 1 >= len(A) or A[i] >= A[i + 1]:
                break
        return i == j and 0 < i < len(A) - 1
