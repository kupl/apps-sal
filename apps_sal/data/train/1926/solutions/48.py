import math


class Solution:
    def closestDivisors(self, num: int) -> List[int]:

        n1 = num + 1
        n2 = num + 2

        def helper(n):
            res = [1, n]
            curr_diff = abs(res[0] - res[1])

            mid = max(int(math.sqrt(n) // 1), 1)
            for i in range(mid, 0, -1):
                if n % i == 0:
                    if abs(i - (n // i)) < curr_diff:
                        res = [i, n // i]
                        curr_diff = abs(i - (n // i))

            return res

        n1_D = helper(n1)
        n2_D = helper(n2)
        n1_D_diff = abs(n1_D[0] - n1_D[1])
        n2_D_diff = abs(n2_D[0] - n2_D[1])

        if n1_D_diff > n2_D_diff:
            return n2_D
        return n1_D
