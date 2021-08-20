class Solution:

    def largestPerimeter(self, A: List[int]) -> int:

        def formT(a, b, c):
            if not a + b > c:
                return False
            if not b + c > a:
                return False
            if not a + c > b:
                return False
            return True
        sides = sorted(A)
        for i in range(len(sides) - 3, -1, -1):
            if formT(sides[i], sides[i + 1], sides[i + 2]):
                return sides[i] + sides[i + 1] + sides[i + 2]
        return 0
