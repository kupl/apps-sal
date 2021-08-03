MOD = 10**9 + 7


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        m = len(locations)
        n = fuel + 1
        mem = [[None for i in range(n)] for j in range(m)]

        return self.backtrack(start, locations, finish, fuel, mem)

    def backtrack(self, cur, locations, finish, fuel, mem):
        if fuel < 0:
            return 0
        elif mem[cur][fuel] != None:
            return mem[cur][fuel]

        count = 0
        if cur == finish:
            count += 1

        for i, pos in enumerate(locations):
            dist = abs(pos - locations[cur])
            if i == cur or dist > fuel:
                continue

            count += self.backtrack(i, locations, finish, fuel - dist, mem)

        mem[cur][fuel] = count % MOD
        return mem[cur][fuel]
