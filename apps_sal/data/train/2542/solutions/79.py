class Solution:
    def isMonotonic(self, A: List[int]) -> bool:

        if (len(A) < 3):
            return True
        gt = False
        lt = False

        for i in range(len(A) - 1):

            if A[i] > A[i + 1]:
                gt = True
            if A[i] < A[i + 1]:
                lt = True
            if (gt and lt):
                return False
        return True
