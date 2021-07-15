class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        point = -1
        for i in range(len(A) - 1, 0, -1):
            if A[i - 1] > A[i]:
                point = i - 1
                break
        if point == -1:
            return A
        right_point = point + 1
        max_val = -1
        for i in range(point + 1, len(A)):
            if A[i] < A[point] and max_val < A[i]:
                right_point = i
                max_val = A[i]
        A[point], A[right_point] = A[right_point], A[point]
        return A
