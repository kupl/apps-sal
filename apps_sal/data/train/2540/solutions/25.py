class Solution:

    def largestPerimeter(self, A: List[int]) -> int:

        def check(x, y, z):
            if x + y > z and y + z > x and (x + z > y):
                return True
            else:
                False
        A = sorted(A)
        A = A[::-1]
        x = A
        print(x)
        lar = 0
        for i in range(len(x) - 2):
            if check(x[i], x[i + 1], x[i + 2]):
                lar = max(lar, x[i] + x[i + 1] + x[i + 2])
        return lar
