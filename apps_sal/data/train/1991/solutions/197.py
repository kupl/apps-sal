class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        mydict = {}

        def func(city, myfuel):
            if myfuel < 0:
                return 0
            if myfuel == 0:
                if city == locations[finish]:
                    return 1
                else:
                    return 0
            tmp = 0
            for i in locations:
                if i != city:
                    if (i, myfuel - abs(i - city)) in mydict:
                        tmp += mydict[(i, myfuel - abs(i - city))]
                    else:
                        tmp += func(i, myfuel - abs(i - city))
            if city == locations[finish]:
                tmp = tmp + 1
            mydict[(city, myfuel)] = tmp
            return tmp

        count = func(locations[start], fuel)
        return (count) % (10**9 + 7)
