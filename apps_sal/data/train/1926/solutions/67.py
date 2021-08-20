import math


class Solution:

    def closestDivisors(self, num: int) -> List[int]:
        d = num
        s = math.ceil(math.sqrt(num))
        while s > 0:
            if s * (num // s) == num + 1 or s * (num // s) == num + 2:
                return [s, num // s]
            elif s * (num // s + 1) == num + 1 or s * (num // s + 1) == num + 2:
                return [s, num // s + 1]
            s -= 1
        return [1, num]
