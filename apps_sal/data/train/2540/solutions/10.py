class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        result = 0
        A = sorted(A)
        for i in range(len(A) - 2):
            a, b, c = A[i], A[i + 1], A[i + 2]
            if (a + b) > c and (a + c) > b and (b + c) > a:
                result = max(result, a + b + c)
        return result
