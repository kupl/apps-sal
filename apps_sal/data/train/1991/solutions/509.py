class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        start_loc = locations[start]
        finish_loc = locations[finish]
        locations.sort()
        start_pos = locations.index(start_loc)
        finish_pos = locations.index(finish_loc)
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(cur_pos: int, left_fuel: int) -> int:
            if abs(locations[cur_pos] - locations[finish_pos]) > left_fuel:
                return 0
            elif abs(locations[cur_pos] - locations[finish_pos]) == left_fuel:
                return (2 ** (abs(cur_pos - finish_pos) - 1)) % (10 ** 9 + 7)

            res = 1 if cur_pos != finish_pos else 0
            next_pos = cur_pos
            while next_pos - 1 >= 0:
                next_pos -= 1
                next_res = dp(next_pos, left_fuel - abs(locations[cur_pos] - locations[next_pos]))
                if next_res:
                    res += next_res
                else:
                    break
            next_pos = cur_pos
            while next_pos + 1 < len(locations):
                next_pos += 1
                next_res = dp(next_pos, left_fuel - abs(locations[cur_pos] - locations[next_pos]))
                if next_res:
                    res += next_res
                else:
                    break

            return res % (10 ** 9 + 7)

        return dp(start_pos, fuel) if start_pos != finish_pos else (dp(start_pos, fuel) + 1) % (10 ** 9 + 7)
