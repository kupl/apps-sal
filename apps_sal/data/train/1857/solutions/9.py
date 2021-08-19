class Solution:

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        (res, lookup) = (0, collections.defaultdict(list))
        for (i, j) in reservedSeats:
            lookup[i].append(j - 1)
        for i in list(lookup.keys()):
            used = False
            available = [1 for j in range(10)]
            for j in lookup[i]:
                available[j] = 0
            for (start, end) in [(1, 5), (5, 9)]:
                if sum(available[start:end]) == 4:
                    res += 1
                    used = True
            if not used and sum(available[3:7]) == 4:
                res += 1
        res += 2 * (n - len(lookup))
        return res
