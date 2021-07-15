class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        dist = [[abs(locations[i]-locations[j]) for j in range(n)] for i in range(n)]
        min_d = [min(dist[i][j] for j in range(n) if j!=i) for i in range(n)]
        memo = {}
        def dp(begin, left):
            if left<min_d[begin]:
                return 1 if begin==finish else 0
            if (begin,left) in memo:
                return memo[(begin,left)]
            memo[(begin,left)] = sum(dp(i,left-dist[begin][i]) for i in range(n) if i!=begin and left>=dist[begin][i])
            if begin==finish:
                memo[(begin,left)] += 1
            return memo[(begin,left)]
        return dp(start,fuel)%(10**9+7)

