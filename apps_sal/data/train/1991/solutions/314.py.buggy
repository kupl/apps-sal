class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        store = {}
        def get(now, fuel):
            name = f\"{now}_{fuel}\"
            if name in store:
                return store[name]
            res = 0
            if now == finish:
                res += 1
            if fuel == 0:
                return res
            for i, j in enumerate(locations):
                if i == now:
                    continue
                if fuel >= abs(locations[i] - locations[now]):
                    res += get(i, fuel - abs(j - locations[now]))
            store[name] = res % 1000000007
            return store[name]
        return get(start, fuel)
