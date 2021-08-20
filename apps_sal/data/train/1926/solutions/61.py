class Solution:

    def closestDivisors(self, num: int) -> List[int]:
        r = int(math.sqrt(num + 2))
        (d, ans) = (inf, [1, num + 1])
        for x in range(r, 1, -1):
            for y in [num + 1, num + 2]:
                if y % x == 0:
                    diff = abs(x - y // x)
                    if d > diff:
                        d = diff
                        ans = [x, y // x]
        return ans
