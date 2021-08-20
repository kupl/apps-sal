class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mem = {}

        def get_val(point, fuel):
            nonlocal finish
            value = mem.get((point, fuel), None)
            if value != None:
                return value
            mem[point, fuel] = 0
            if point == finish:
                mem[point, fuel] = 1
            for i in range(len(locations)):
                if i != point:
                    if fuel - abs(locations[i] - locations[point]) >= 0:
                        mem[point, fuel] += get_val(i, fuel - abs(locations[i] - locations[point]))
            return mem[point, fuel]
        v = get_val(start, fuel)
        return v % (10 ** 9 + 7)
