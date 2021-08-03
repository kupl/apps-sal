class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        memo = {}

        def find(curr, fuel):
            if fuel < 0:
                return 0
            ans = 0
            s = str(curr) + ' ' + str(fuel)
            if s in memo:
                return memo[s]
            if curr == finish:
                ans += 1

            for i in range(len(locations)):
                nextcity = i
                if nextcity != curr:
                    ans += find(nextcity, fuel - abs(locations[curr] - locations[i]))
                    ans %= 10**9 + 7

            memo[s] = ans
            return ans

        return find(start, fuel)
