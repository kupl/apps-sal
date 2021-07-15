class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        cost = lambda i,j: abs(locations[i]-locations[j])
        @lru_cache(None)
        def dfs(i, f):
            if f < abs(cost(i, finish)): return 0
            # if f<0: return 0 
            return sum([dfs(j,f-cost(i,j)) for j in range(len(locations)) if j != i]) + (i==finish)
        return dfs(start, fuel) % (10**9+7)

    def countRoutes1(self, L: List[int], st: int, end: int, f: int) -> int:
        M=10**9+7
        res=0
        def dfs(st,end,f):
            for i,c in enumerate(L):
                need=abs(c-L[st])
                if need <= f:
                    if i==end:
                        res+=1
                    else:
                        if need<f: dfs(i,end,f-need)
        dfs(st,end,f)
        return res%M
