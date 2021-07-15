class Solution:
    def countRoutes(self, A: List[int], start: int, finish: int, fuel: int) -> int:
        
        mod = 10 ** 9 + 7
        
        d = {}
        t = {}
        for i, ele in enumerate(A):
            d[i] = ele
            t[ele] = i
        
        nums = sorted(A)
        
        @lru_cache(None)
        def dp(i, j, f):
            if not f:
                return i == j
            loc = d[i]
            l, r = bisect.bisect_left(nums, loc - f), bisect.bisect_right(nums, loc + f)
            res = (1 if i == j else 0)
            for ele in nums[l:r]:
                if ele != loc:
                    res += dp(t[ele], j, f - abs(ele - loc)) % mod
            return res
        
        return dp(start, finish, fuel) % mod
