class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        res, lookup = 0, collections.defaultdict(set)
        for i, j in reservedSeats:
            lookup[i].add(j)
        for i in list(lookup.keys()):
            used = False
            for start, end in [(2, 6), (6, 10)]:
                if all(j not in lookup[i] for j in range(start, end)):
                    res += 1
                    used = True
            if not used and all(j not in lookup[i] for j in range(4, 8)):
                res += 1
        res += 2 * (n - len(lookup))
        return res
