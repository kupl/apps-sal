class Solution:
    def countRoutes(self, nums: List[int], start: int, finish: int, fuel: int) -> int:
        def dp(i, f, cache):
            if f < 0:
                return 0
            if f == 0:
                return 1 if i == finish else 0
            if (i, f) not in cache:
                ans = 1 if i == finish else 0
                for j in range(len(nums)):
                    if j != i:
                        ans += dp(j, f - abs(nums[i] - nums[j]), cache)
                cache[(i, f)] = ans
            return cache[(i, f)]

        return dp(start, fuel, {}) % (10 ** 9 + 7)
