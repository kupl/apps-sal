class Solution:

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        res = 0
        d = defaultdict(set)
        for (x, y) in reservedSeats:
            d[x - 1].add(y - 1)
        for r in d.keys():
            if all((x not in d[r] for x in [1, 2, 3, 4])):
                res += 1
                for x in [1, 2, 3, 4]:
                    d[r].add(x)
            if all((x not in d[r] for x in [3, 4, 5, 6])):
                res += 1
                for x in [3, 4, 5, 6]:
                    d[r].add(x)
            if all((x not in d[r] for x in [5, 6, 7, 8])):
                res += 1
                for x in [5, 6, 7, 8]:
                    d[r].add(x)
        return res + 2 * (n - len(d.keys()))
