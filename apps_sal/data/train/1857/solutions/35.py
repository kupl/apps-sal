from collections import defaultdict


class Solution:

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        i = 0
        prev = 1
        res = set()
        ans = 0
        res = defaultdict(list)
        for i in range(len(reservedSeats)):
            res[reservedSeats[i][0] - 1].append(reservedSeats[i][1])
        count_rows = 0
        helper = [0 for i in range(10)]
        for i in res.keys():
            count_rows += 1
            count = 0
            for j in range(10):
                helper[j] = 0
            for j in res[i]:
                helper[j - 1] = 1
            if helper[1:5] == [0, 0, 0, 0]:
                count += 1
            if helper[5:9] == [0, 0, 0, 0]:
                count += 1
            if count == 0 and helper[3:7] == [0, 0, 0, 0]:
                count += 1
            ans += count
        ans += (n - count_rows) * 2
        return ans
