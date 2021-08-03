class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        i = 1
        while i < (num + 2)**0.5 + 1:
            if ((num + 1) % i) == 0:
                res = [i, (num + 1) // i]

            if ((num + 2) % i) == 0:
                if abs(i - (num + 2) // i) < abs(res[0] - res[1]):
                    res = [i, (num + 2) // i]
            i += 1
        return res
