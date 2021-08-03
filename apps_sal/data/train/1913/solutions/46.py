class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        def findLarger():
            prev = A[-1]
            for i in range(len(A) - 1, -1, -1):
                if A[i] > prev:
                    return i
                prev = A[i]
            return -1
        if not A:
            return A
        larger = findLarger()
        if larger == -1:
            return A
        sl = larger + 1
        for i in range(larger, len(A)):
            if A[i] < A[larger]:
                if A[sl] < A[i]:
                    sl = i
        print((larger, sl))
        A[sl], A[larger] = A[larger], A[sl]
        return A
