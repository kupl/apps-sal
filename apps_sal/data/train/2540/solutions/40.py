class Solution:
    def largestPerimeter(self, A: List[int]) -> int:

        def area(a, b, c):
            s = (a + b + c) / 2

            val = (s * (s - a) * (s - b) * (s - c))**(1 / 2)
            if isinstance(val, complex):
                return 0
            return val

        A.sort()
        maxi = 0

        for i in range(len(A) - 2):
            val = area(A[i], A[i + 1], A[i + 2])

            if val != 0:
                p = (A[i] + A[i + 1] + A[i + 2])
                if p > maxi:
                    maxi = p

        return maxi
