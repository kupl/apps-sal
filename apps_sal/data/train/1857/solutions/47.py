class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        matrix = collections.defaultdict(list)
        for i in range(len(reservedSeats)):
            matrix[reservedSeats[i][0]].append(reservedSeats[i][1])

        res = 2 * n
        for k in matrix:
            cnt = 0
            if 2 not in matrix[k] and 3 not in matrix[k] and 4 not in matrix[k] and 5 not in matrix[k]:
                cnt += 1
            if 6 not in matrix[k] and 7 not in matrix[k] and 8 not in matrix[k] and 9 not in matrix[k]:
                cnt += 1
            if 4 not in matrix[k] and 5 not in matrix[k] and 6 not in matrix[k] and 7 not in matrix[k] and cnt == 0:
                cnt += 1
            res += (cnt - 2)

        return res
