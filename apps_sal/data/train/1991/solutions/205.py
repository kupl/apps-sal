def neigh(start, locations, fuel):
    res = []
    n = len(locations)
    for j in range(n):
        i = locations[j]
        if(j == start):
            continue
        if(abs(i - locations[start]) <= fuel):
            res.append(j)
    return res


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        if(abs(locations[finish] - locations[start]) > fuel):
            # print(fuel,abs(locations[finish]-locations[start]))
            return 0
        n = len(locations)
        dp = [[-1 for i in range(fuel + 1)] for j in range(n)]

        def dfs(start, fuel):
            if(fuel < 0):
                return 0
            if(dp[start][fuel] != -1):
                return dp[start][fuel]
            neighs = neigh(start, locations, fuel)
            # print(start,neighs,fuel)
            count = 0
            if(start == finish):
                count += 1
            for i in neighs:
                count += (dfs(i, fuel - abs(locations[start] - locations[i])))
            dp[start][fuel] = count
            return count
        return dfs(start, fuel) % (pow(10, 9) + 7)
