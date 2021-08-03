import numpy as np

MOD = 10 ** 9 + 7
cache = None
locations = None


def count(current, finish, fuel):
    if cache[current, fuel] >= 0:
        return cache[current, fuel]

    if abs(locations[current] - locations[finish]) > fuel:
        cache[current, fuel] = 0
        return 0

    routes = 1 if current == finish else 0
    for i in range(0, len(locations)):
        if i == current:
            continue

        distance = abs(locations[current] - locations[i])
        remaining = fuel - distance
        if remaining >= 0:
            routes += count(i, finish, remaining)

    cache[current, fuel] = routes % MOD
    return cache[current, fuel]


class Solution:
    def countRoutes(self, locs: List[int], start: int, finish: int, fuel: int) -> int:
        nonlocal cache, locations
        locations = locs
        cache = np.full((len(locations), fuel + 1), -1)
        return count(start, finish, fuel)
