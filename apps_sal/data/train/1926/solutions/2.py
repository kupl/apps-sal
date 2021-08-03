
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def divisors(n):
            for i in range(int((n + 2)**0.5), 0, -1):
                if (n + 1) % i == 0:
                    return [i, (n + 1) // i]
                if (n + 2) % i == 0:
                    return [i, (n + 2) // i]
            return [1, n + 1]

        return divisors(num)
