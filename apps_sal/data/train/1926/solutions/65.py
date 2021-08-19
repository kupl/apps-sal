class Solution:

    def closestDivisors(self, num: int) -> List[int]:
        sqrt = int(num ** 0.5) + 1
        for i in range(sqrt, 0, -1):
            j1 = (num + 1) // i
            j2 = (num + 2) // i
            d1 = d2 = sys.maxsize
            if j1 * i == num + 1:
                d1 = abs(j1 - i)
            if j2 * i == num + 2:
                d2 = abs(j2 - i)
            if d1 != sys.maxsize or d2 != sys.maxsize:
                return [j1, i] if d1 < d2 else [j2, i]
        return []
