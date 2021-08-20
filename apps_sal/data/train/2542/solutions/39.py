class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        if min(A) == A[0]:
            start = 0
            increment = 1
            end = len(A)
        elif max(A) == A[0]:
            start = len(A) - 1
            increment = -1
            end = 0
        else:
            return False
        num = A[start]
        print(start, num)
        for i in range(start, end, increment):
            print(A[i], num)
            if A[i] < num:
                return False
            num = A[i]
        return True
