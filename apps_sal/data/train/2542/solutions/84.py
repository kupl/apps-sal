class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        flag = None
        for i in zip(A, A[1:]):
            temp = i[1] - i[0]
            if flag:
                if flag * temp < 0:
                    return False
            elif temp > 0:
                flag = 1
            elif temp < 0:
                flag = -1
        return True
