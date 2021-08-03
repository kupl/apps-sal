import math


class Solution:
    def helper(self, num):
        sqrt = int(math.sqrt(num))
        gmin = float('inf')
        ans = None
        for i in range(1, sqrt + 1):
            if num % i == 0 and abs(i - num / i) < gmin:
                gmin = abs(i - num / i)
                ans = [i, int(num / i)]
        return ans

    def closestDivisors(self, num: int) -> List[int]:
        ans1 = self.helper(num + 1)
        ans2 = self.helper(num + 2)
        if ans1 == None:
            return ans2
        elif ans2 == None:
            return ans1
        if abs(ans1[0] - ans1[1]) < abs(ans2[0] - ans2[1]):
            return ans1
        return ans2
