class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10 ** 9 + 7
        memo = {}

        def dp(pos, leftFuel):
            if memo.get((pos, leftFuel), None) is not None:
                return memo[pos, leftFuel]
            ans = 0
            if pos == finish:
                ans = 1
            for otherPos in range(len(locations)):
                if pos != otherPos and abs(locations[pos] - locations[otherPos]) <= leftFuel:
                    ans += dp(otherPos, leftFuel - abs(locations[pos] - locations[otherPos]))
            memo[pos, leftFuel] = ans
            return ans
        ans = dp(start, fuel) % mod
        return ans
