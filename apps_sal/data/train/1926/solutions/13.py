def f(n):
    for i in range(int(n**.5), 0, -1):
        if n % i == 0:
            return [i, n // i]


class Solution:
    def closestDivisors(self, n: int) -> List[int]:
        a, b = f(n + 1), f(n + 2)
        return a if abs(a[1] - a[0]) < abs(b[0] - b[1]) else b
