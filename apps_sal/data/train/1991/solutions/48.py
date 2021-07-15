class Solution:
    def countRoutes(self, loc: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(None)
        def get(cur, left):
            if left < 0: return 0
            return (sum([get(i, left-abs(loc[i]-loc[cur])) for i in range(len(loc)) if i != cur]) + (cur==finish)) % 1000000007
        return get(start, fuel)
