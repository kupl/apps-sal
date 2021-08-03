MOD = 10**9 + 7


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        self.finish = finish
        self.locations = locations
        mem = {}

        res = self.dp(start, fuel, mem)
        return res % MOD

    def dp(self, st, fuel, mem):

        if (st, fuel) in mem:
            return mem[(st, fuel)]

        res = 1 if st == self.finish else 0

        for mid in range(len(self.locations)):

            if mid == st:
                continue

            if abs(self.locations[mid] - self.locations[st]) > fuel:
                continue

            res += self.dp(mid, fuel - abs(self.locations[mid] - self.locations[st]), mem)

        mem[(st, fuel)] = res

        return res
