class Solution:

    def closestDivisors(self, num: int) -> List[int]:
        (x, y) = self.get_factors(num + 1)
        (z, t) = self.get_factors(num + 2)
        print((x, y), (z, t))
        return [x, y] if abs(x - y) <= abs(z - t) else [z, t]

    def get_prime_numbers_below(self, n):
        numbers = set([i for i in range(2, n)])
        for i in range(2, int(sqrt(n)) + 1):
            j = max(2, i)
            while i * j < n:
                if i * j in numbers:
                    numbers.remove(i * j)
                j += 1
        return list(numbers)

    def get_factors(self, n):
        y = n
        for x in range(1, int(sqrt(n)) + 1):
            y = int(n / x) if (n / float(x)).is_integer() else y
        return (int(n / y), y)
