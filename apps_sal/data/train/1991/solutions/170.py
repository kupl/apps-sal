class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        '''
        [2,3,6,8,4]
        start = 1
        fin = 3
        fuel = 5

        '''
        ref = defaultdict(list)
        # for i in range(len(locations)):
        #     for j in range(len(locations)):
        #         if i == j: continue
        #         ref[locations[i]].append((locations[j], abs(locations[i]-locations[j])))
        #     ref[locations[i]].sort()

        from functools import lru_cache
        finish = locations[finish]
        MOD = 10**9 + 7
        mycache = {}

        def solve(pos, rfuel):
            # print(pos, rfuel)
            if (pos, rfuel) in mycache:
                return mycache[(pos, rfuel)]
            sol = 0
            if pos == finish:
                sol += 1
            for it in locations:
                if it == pos:
                    continue
                tup = (it, abs(pos - it))
                if tup[1] <= rfuel:
                    sol += solve(tup[0], rfuel - tup[1])
            mycache[(pos, rfuel)] = sol % MOD
            return sol

        solve(locations[start], fuel)
        # print(locations)
        # print('mycache', mycache)
        return mycache[(locations[start], fuel)] % MOD
