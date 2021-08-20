class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        shortest = {finish: 0}
        ans = 0
        heap = sorted([[abs(locations[i] - locations[finish]), i] for i in range(len(locations))])
        while len(shortest) < len(locations):
            (d, i) = heapq.heappop(heap)
            if i in shortest:
                continue
            shortest[i] = d
            for j in range(len(locations)):
                if j not in shortest and j != finish:
                    heapq.heappush(heap, [abs(locations[j] - locations[i]) + d, j])

        @lru_cache(None)
        def dfs(cur, fuel):
            if fuel < shortest[cur]:
                return 0
            if fuel == 0:
                if cur != finish:
                    return 0
                else:
                    return 1
            ans = 0
            if cur == finish:
                ans += 1
            for i in range(len(locations)):
                cost = abs(locations[i] - locations[cur])
                if i != cur and cost <= fuel:
                    ans += dfs(i, fuel - cost) % 1000000007
            return ans % 1000000007
        return dfs(start, fuel)
