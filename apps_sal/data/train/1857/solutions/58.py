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
        four_person = [0, 0, 0, 0]
        for data in lookup.values():
            data_tup = tuple(data)
            if data_tup not in dic:
                prev = res
                if data[1:5] == four_person:
                    res += 1
                    if data[5:9] == four_person:
                        res += 1
                elif data[3:7] == four_person or data[5:9] == four_person:
                    res += 1
                dic[data_tup] = res - prev
            else:
                res += dic[data_tup]
        return res + 2 * (n - len(lookup))
