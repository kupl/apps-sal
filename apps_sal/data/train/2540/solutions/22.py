class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        for a, b, c in zip(A, A[1:], A[2:]):
            if a < b + c:
                return(a + b + c)
            else:
                continue
        return (0)
