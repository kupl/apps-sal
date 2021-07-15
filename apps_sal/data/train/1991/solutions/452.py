class Solution:
    def countRoutes(self, l: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 1000000007
        N = len(l)
        nways = [[0]*(fuel+1) for _ in range(N)]
        nways[start][0] = 1
        for f in range(1, fuel+1): 
            for to in range(N): 
                for fr in range(N): 
                    c = abs(l[to] - l[fr])
                    if to==fr or f < c: 
                        continue
                    nways[to][f] += nways[fr][f - c]
        return sum(nways[finish]) % mod
            

