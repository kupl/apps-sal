class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) <= 1:
            return True

        flag = -1

        if A[0] < A[1]:
            flag = 0
        elif A[0] == A[1]:
            flag = 1
        else:
            flag = 2

        for i in range(0, len(A) - 1):
            if flag == 0 and A[i] > A[i + 1]:
                return False
            elif flag == 2 and A[i] < A[i + 1]:
                return False
            elif flag == 1:
                if A[i] > A[i + 1]:
                    flag = 2
                elif A[i] < A[i + 1]:
                    flag = 0
                else:
                    flag = 1

        return True
