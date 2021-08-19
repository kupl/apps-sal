import math


class Solution:

    def closestDivisors(self, num: int) -> List[int]:
        for x in range(int(math.sqrt(num + 2)), 0, -1):
            if (num + 1) % x == 0:
                return [x, (num + 1) // x]
            if (num + 2) % x == 0:
                return [x, (num + 2) // x]
