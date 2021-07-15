class Solution:
    def countRoutes(self, locations, start: int, finish: int, fuel: int) -> int:
        KMAX = 10 ** 9 + 7
        N = len(locations)
        mem = dict()
        
        def dp(city, gas):
            if (city, gas) in mem:
                return mem[city, gas]
            if gas < 0:
                return 0
            mem[city, gas] = 1 if city == finish else 0
            for i in range(N):
                if i == city or abs(locations[i] - locations[city]) > gas:
                    continue
                mem[city, gas] += dp(i, gas - abs(locations[i] - locations[city]))
            return mem[city, gas]
        res = dp(start, fuel) % KMAX
        return res

