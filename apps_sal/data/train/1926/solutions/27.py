class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        if num == 1:
            return [1, 2]
        a = num + 1
        b = num + 2
        adiv = []
        bdiv = []
        for i in range(1, int(math.sqrt(b) + 1)):
            if a % i == 0:
                min_a = abs(a // i - i)
                adiv.append([min_a, b // i, i])
            if b % i == 0:
                min_b = abs(b // i - i)
                adiv.append([min_b, b // i, i])

        m = min(adiv)
        return [m[1], m[2]]
