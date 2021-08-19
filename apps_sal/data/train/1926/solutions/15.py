class Solution:

    def closestDivisors(self, num: int) -> List[int]:
        N1 = num + 1
        N2 = num + 2
        sqrt1 = int(N1 ** 0.5) + 1
        sqrt2 = int(N2 ** 0.5) + 1
        while sqrt1 >= 2 or sqrt2 >= 2:
            if N2 % sqrt2 == 0:
                return [sqrt2, int(N2 / sqrt2)]
            if N1 % sqrt1 == 0:
                return [sqrt1, int(N1 / sqrt1)]
            else:
                sqrt1 -= 1
                sqrt2 -= 1
        return [1, sqrt1]
