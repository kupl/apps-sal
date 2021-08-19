class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        found = {}

        def count(cstart, cfuel):
            if (cstart, cfuel) in found:
                return found[cstart, cfuel]
            if cfuel < 0:
                return 0
            if cfuel == 0:
                return cstart == finish
            r = int(cstart == finish)
            for (i, l) in enumerate(locations):
                if i != cstart:
                    r += count(i, cfuel - abs(locations[i] - locations[cstart]))
            found[cstart, cfuel] = r % (10 ** 9 + 7)
            return found[cstart, cfuel]
        return count(start, fuel)
