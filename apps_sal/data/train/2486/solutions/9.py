class Solution:

    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        ans = 0
        while num != 0:
            if num & 1 == 0:
                num = num >> 1
                ans += 1
            else:
                if num == 1:
                    return ans + 1
                num = num >> 1
                ans += 2
        return ans
