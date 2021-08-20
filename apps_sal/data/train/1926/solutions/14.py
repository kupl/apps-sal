class Solution:

    def closestDivisors(self, num: int) -> List[int]:

        def find(n):
            for i in range(int(n ** 0.5), 0, -1):
                if n % i == 0:
                    return (i, n // i)
            return (None, None)
        (a, b) = find(num + 1)
        (c, d) = find(num + 2)
        return [a, b] if b - a < d - c else [c, d]
