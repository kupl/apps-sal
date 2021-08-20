class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10 ** 9 + 7

        @lru_cache(None)
        def count_paths(index, fuel):
            total = 0
            if fuel < 0:
                return 0
            if index == finish:
                total += 1
            current = locations[index]
            for (next_index, x) in enumerate(locations):
                if next_index != index:
                    total += count_paths(next_index, max(-1, fuel - abs(current - x)))
            return total
        answer = count_paths(start, fuel)
        return answer % mod
