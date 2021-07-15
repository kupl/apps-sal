class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @functools.lru_cache(None)
        def dp(pos,fuel):
            res=1 if pos==locations[finish] else 0
            for nxt in locations:
                if nxt==pos or fuel<abs(nxt-pos):
                    continue
                res+=dp(nxt,fuel-abs(nxt-pos))
            return res%(10**9+7)
        return dp(locations[start],fuel)

