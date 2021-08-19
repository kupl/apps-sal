class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dic = defaultdict(lambda: defaultdict(lambda: 0))
        dic[fuel] = {start: 1}
        ans = 0
        mod = 10 ** 9 + 7
        for f in range(fuel, -1, -1):
            for (j, r) in list(dic[f].items()):
                for i in range(len(locations)):
                    if j != i:
                        meh = f - abs(locations[j] - locations[i])
                        if meh >= 0:
                            dic[meh][i] = (dic[meh][i] + r) % mod
            ans = (ans + dic[f - 1][finish]) % mod
        return ans + (start == finish)
