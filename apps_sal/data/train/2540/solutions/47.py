class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        for i in range(len(A) - 2):
            a, b, c = A[i], A[i + 1], A[i + 2]
            c1 = a + b > c
            c2 = b + c > a
            c3 = c + a > b
            if c1 and c2 and c3:
                return a + b + c

        return 0
