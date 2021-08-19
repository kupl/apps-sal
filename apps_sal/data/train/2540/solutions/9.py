class Solution:

    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A)
        perimeter = 0
        for i in range(len(A) - 2):
            (s1, s2, s3) = (A[i], A[i + 1], A[i + 2])
            p = s1 + s2 + s3
            if s1 + s2 > s3 and s2 + s3 > s1 and (s1 + s3 > s2):
                perimeter = max(perimeter, p)
        return perimeter
