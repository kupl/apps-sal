class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mem = {}

        def dfs(idx, currFuel):
            key = (idx, currFuel)
            if key in mem:
                return mem[key]
            if currFuel < 0:
                return 0
            res = 1 if idx == finish else 0
            for i in range(len(locations)):
                if i != idx:
                    res += dfs(i, currFuel - abs(locations[idx] - locations[i]))
            mem[key] = res
            return mem[key]
        return dfs(start, fuel) % (10**9 + 7)
