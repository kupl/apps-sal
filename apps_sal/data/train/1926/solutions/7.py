class Solution:

    def closestDivisors(self, num: int) -> List[int]:
        for d in range(int((num + 2) ** 0.5), 0, -1):
            if (num + 1) % d == 0:
                return [d, (num + 1) // d]
            if (num + 2) % d == 0:
                return [d, (num + 2) // d]
