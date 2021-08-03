class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        num_paths = [[0 for _ in locations] for _ in range(fuel + 1)]
        mod_constant = 10 ** 9 + 7

        num_paths[0][finish] = 1
        for this_fuel in range(1, fuel + 1):
            for i, loci in enumerate(locations):
                this_num_paths = 0
                for j, locj in enumerate(locations):
                    if i == j:
                        continue
                    if abs(loci - locj) <= this_fuel:
                        this_num_paths = (this_num_paths + num_paths[this_fuel - abs(loci - locj)][j]) % mod_constant
                num_paths[this_fuel][i] = this_num_paths

        total_num_paths = 0
        for this_fuel in range(fuel + 1):
            total_num_paths = (total_num_paths + num_paths[this_fuel][start]) % mod_constant
        return total_num_paths
