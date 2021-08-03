class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        up = False
        if A[0] < A[len(A) - 1]:
            up = True
        elif A[0] > A[len(A) - 1]:
            up = False

        for i in range(len(A) - 1):
            if up:
                print((A[i], A[i + 1]))
                if A[i] > A[i + 1]:
                    return False
            else:
                if A[i] < A[i + 1]:
                    return False
        return True
