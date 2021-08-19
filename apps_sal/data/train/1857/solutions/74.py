class Solution:

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        h = defaultdict(list)
        res = 0
        for k in reservedSeats:
            h[k[0]].append(k[1])
        for i in list(h.keys()):
            row = h[i]
            if len(row) == 1:
                if row[0] == 1 or row[0] == 10:
                    res += 2
                else:
                    res += 1
            else:
                seats = [0] * 10
                for i in row:
                    seats[i - 1] = 1
                res_copy = res
                if seats[1:5] == [0, 0, 0, 0]:
                    res += 1
                if seats[5:9] == [0, 0, 0, 0]:
                    res += 1
                if res_copy == res and seats[3:7] == [0, 0, 0, 0]:
                    res += 1
        return res + 2 * (n - len(list(h.keys())))
