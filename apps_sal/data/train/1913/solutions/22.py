class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        if not A:
            return A

        leftIndex = -1
        for i in range(len(A) - 1, 0, -1):
            if A[i - 1] > A[i]:
                leftIndex = i - 1
                break

        if leftIndex == -1:
            return A

        rightIndex = -1
        for i in range(len(A) - 1, leftIndex, -1):
            if A[i] >= A[leftIndex]:
                continue
            elif rightIndex == -1:
                rightIndex = i
            elif A[i] == A[rightIndex]:
                rightIndex = i

        A[leftIndex], A[rightIndex] = A[rightIndex], A[leftIndex]
        return A
