class Solution:
    def numberOfSteps (self, num: int) -> int:
        cnt = 0
        while num:
            if num & 1: num -= 1
            else: num >>= 1
            cnt += 1
        return cnt
