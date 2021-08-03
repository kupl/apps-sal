class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        def recurssion(start, finish, fuel):
            if fuel < 0:
                return 0
            if fuel == 0 and start == finish:
                return 1
            res = 0
            for i in range(l):
                if i != start:
                    if fuel - abs(locations[i] - locations[start]) < 0:
                        continue
                    if (i, finish, fuel - abs(locations[i] - locations[start])) in ht:
                        r = ht[(i, finish, fuel - abs(locations[i] - locations[start]))]
                    else:
                        r = recurssion(i, finish, fuel - abs(locations[i] - locations[start]))
                    if r > 0:
                        res += r
            # print(start,finish,fuel,res)
            if (start, finish, fuel) not in ht:
                ht[(start, finish, fuel)] = res
                ht[(finish, start, fuel)] = res
            return res

        ht = {}
        l = len(locations)
        res = 0
        for i in range(fuel + 1):
            res += recurssion(start, finish, i)
        return res % 1000000007
