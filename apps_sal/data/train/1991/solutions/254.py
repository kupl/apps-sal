class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # DFS
        self.N = len(locations)
        self.finish = finish
        self.M = dict()
        def dfs(i, f):
            if (i, f) not in self.M:
                res = 0
                if i == self.finish:
                    res += 1
                for j in range(self.N):
                    if j != i and f >= abs(locations[i] - locations[j]):
                        res += dfs(j, f - abs(locations[i] - locations[j]))
                self.M[(i, f)] = res
            return self.M[(i, f)]
        
        return dfs(start, fuel) % (10**9 + 7) 
