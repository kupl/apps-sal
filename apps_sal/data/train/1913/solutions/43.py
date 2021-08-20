class Solution:

    def prevPermOpt1(self, A: List[int]) -> List[int]:
        """
        5,6,1,1,1
        5,1,6,2,1
        """
        for i in reversed(range(1, len(A))):
            if A[i - 1] > A[i]:
                maxLessInd = i
                maxLessVal = A[i]
                for j in range(i + 1, len(A)):
                    if A[j] > maxLessVal and A[j] < A[i - 1]:
                        maxLessVal = A[j]
                        maxLessInd = j
                (A[i - 1], A[maxLessInd]) = (A[maxLessInd], A[i - 1])
                return A
        return A
