class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        dic = []

        n = len(locations)

        for i in range(n):

            dic.append([None] * (fuel + 1))

        def dp(l, s, f, fuel, dic, n):

            if(fuel == 0):
                if(s == f):
                    return 1
                return 0

            if(dic[s][fuel] != None):
                return dic[s][fuel]

            number = 0

            if(s == f):
                number = 1

            for i in range(n):

                if(i != s):
                    if(abs(l[i] - l[s]) <= fuel):
                        number += dp(l, i, f, fuel - abs(l[i] - l[s]), dic, n)

            dic[s][fuel] = number

            return number

        return dp(locations, start, finish, fuel, dic, n) % 1000000007
