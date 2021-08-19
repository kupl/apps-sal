class Solution:

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        lookup = collections.defaultdict(list)
        dic = {}
        for (row, seat) in reservedSeats:
            if row - 1 not in lookup:
                data = [0] * 10
                data[seat - 1] = 1
                lookup[row - 1] = data
            else:
                lookup[row - 1][seat - 1] = 1
        res = 0
        for k in lookup:
            data_tup = tuple(lookup[k])
            if data_tup not in dic:
                prev = res
                first = third = False
                if lookup[k][1] or lookup[k][2] or (lookup[k][1] and lookup[k][2]):
                    if sum(lookup[k][3:7]) == 0 or sum(lookup[k][5:9]) == 0:
                        res += 1
                else:
                    if sum(lookup[k][1:5]) == 0:
                        res += 1
                        first = True
                    if sum(lookup[k][5:9]) == 0:
                        res += 1
                        third = True
                    if not first and (not third) and (sum(lookup[k][3:7]) == 0):
                        res += 1
                dic[data_tup] = res - prev
            else:
                res += dic[data_tup]
        return res + 2 * (n - len(lookup))
