class Solution:

    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A)
        while True:
            if A[-1] + A[-2] > A[-3] and A[-1] + A[-3] > A[-2] and (A[-3] + A[-2] > A[-1]):
                return A[-1] + A[-2] + A[-3]
            A.remove(A[-1])
            if len(A) == 2:
                return 0
