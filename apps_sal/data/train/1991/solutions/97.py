class Solution:
    #1575
    #1575
    def countRoutes(self, locations: 'List[int]', start: int, finish: int, fuel: int) -> int:
        MOD = 1000000007
        sp,ep = locations[start], locations[finish]
        locations.sort()
        s, e = locations.index(sp), locations.index(ep)
        if s > e: s,e=e,s
        N = len(locations)
        @functools.lru_cache(None)
        def helper(i, f):
            if i!=e and locations[e]-locations[i] <= f:
                res = 1
            else:
                res = 0
            k = i-1
            while k>=0 and locations[i]+locations[e]-2*locations[k] <= f:
                res += helper(k, f-(locations[i]-locations[k]))
                k -= 1
            k = i + 1
            while k<N and locations[k]-locations[i]+abs(locations[k]-locations[e]) <= f:
                res += helper(k, f-(locations[k]-locations[i]))
                k += 1
            return res%MOD
        return helper(s,fuel) + (s==e)
