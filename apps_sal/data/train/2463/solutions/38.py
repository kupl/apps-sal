class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        passedPeak = False

        if len(A) <= 2 or A[0] > A[1]:
            return False

        for i in range(len(A) - 1):
            if A[i] == A[i + 1]:
                return False

            if passedPeak == True and A[i] < A[i + 1]:
                return False

            if passedPeak == False and A[i] > A[i + 1]:
                passedPeak = True

        if passedPeak:
            return True
        else:
            return False
