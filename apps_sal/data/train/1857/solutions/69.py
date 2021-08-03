from collections import defaultdict


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        d = defaultdict(set)
        for r in reservedSeats:
            d[r[0] - 1].add(r[1] - 1)
        ans = 0
        for i in list(d.keys()):
            j = 0
            while j < 7:
                if j in [1, 3, 5]:
                    if j not in d[i] and j + 1 not in d[i] and j + 2 not in d[i] and j + 3 not in d[i]:
                        ans += 1
                        j += 4
                        continue
                j += 1
        return ans + 2 * (n - len(list(d.keys())))
