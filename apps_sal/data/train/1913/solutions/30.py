class Solution:

    def prevPermOpt1(self, A: List[int]) -> List[int]:
        largest = len(A) - 2
        while largest >= 0 and A[largest] <= A[largest + 1]:
            largest -= 1
        if largest == -1:
            return A
        smallest = len(A) - 1
        while A[largest] <= A[smallest]:
            smallest -= 1
        f = smallest
        while A[smallest] == A[f]:
            f -= 1
        (A[f + 1], A[largest]) = (A[largest], A[f + 1])
        return A
