class Solution:
    def isMonotonic(self, A: List[int]) -> bool:

        # initial value
        mono = 0

        for i in range(len(A) - 1):
            if A[i + 1] - A[i] != 0:
                if mono == 0:
                    mono = A[i + 1] - A[i]
                else:
                    if mono * (A[i + 1] - A[i]) < 0:
                        return False

        return True
