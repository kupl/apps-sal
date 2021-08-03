class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        res = [-math.inf, math.inf]
        min_dist = math.inf
        for i in range(1, int(math.sqrt(num + 1)) + 2):
            if (num + 1) % i == 0:
                if ((num + 1) // i) - i < min_dist:
                    res = [i, (num + 1) // i]
                    min_dist = (num + 2) // i - i
        for i in range(1, int(math.sqrt(num + 2)) + 2):
            if (num + 2) % i == 0:
                if ((num + 2) // i) - i < min_dist:
                    res = [i, (num + 2) // i]
                    min_dist = (num + 2) // i - i
        return res
