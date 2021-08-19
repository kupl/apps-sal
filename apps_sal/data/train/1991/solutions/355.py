MAX = int(10 ** 9 + 7)


class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        A = [[None for _ in range(fuel + 1)] for _ in range(len(locations))]
        A[start][fuel] = 1
        for f in range(fuel, 0, -1):
            for ca in range(len(locations) - 1, -1, -1):
                if A[ca][f] is None:
                    continue
                for cb in range(len(locations) - 1, -1, -1):
                    if cb == ca:
                        continue
                    loss = int(abs(locations[ca] - locations[cb]))
                    if loss > f:
                        continue
                    A[cb][f - loss] = ((A[cb][f - loss] or 0) + A[ca][f]) % MAX
        r = 0
        for x in A[finish]:
            if x is None:
                continue
            r = (r + x) % MAX
        return r
