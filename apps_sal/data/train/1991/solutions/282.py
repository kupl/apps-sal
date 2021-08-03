class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        def back_track(ci, fuel, N, mem):
            if (ci, fuel) in mem:
                return mem[(ci, fuel)]
            res = 0
            for i in range(N):
                if i != ci:
                    if fuel - abs(locations[ci] - locations[i]) >= 0:
                        res += (1 if i == finish else 0) + back_track(i, fuel - abs(locations[ci] - locations[i]), N, mem)
            mem[(ci, fuel)] = res
            return mem[(ci, fuel)]

        return (back_track(start, fuel, len(locations), defaultdict()) + (1 if start == finish else 0)) % (10**9 + 7)
