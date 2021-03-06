class Solution:

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedSeats.sort()
        matrix = {}
        for i in range(len(reservedSeats)):
            k = reservedSeats[i][0]
            if k in matrix:
                matrix[k].append(reservedSeats[i][1])
            else:
                matrix[k] = [reservedSeats[i][1]]
        res = 2 * n
        for (k, v) in matrix.items():
            left_group = mid_group = right_group = True
            if 2 in v or 3 in v:
                left_group = False
            if 4 in v or 5 in v:
                left_group = False
                mid_group = False
            if 6 in v or 7 in v:
                mid_group = False
                right_group = False
            if 8 in v or 9 in v:
                right_group = False
            if left_group or right_group:
                mid_group = False
            res -= 2 - (left_group + mid_group + right_group)
        return res
