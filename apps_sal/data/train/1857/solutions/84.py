class Solution:

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedSeats.sort()
        count = 2 * (reservedSeats[0][0] - 1)
        row_start = 0
        while row_start < len(reservedSeats):
            row_end = row_start
            indices = []
            while row_end < len(reservedSeats) and reservedSeats[row_end][0] == reservedSeats[row_start][0]:
                indices.append(reservedSeats[row_end][1])
                row_end += 1
            if len(indices) == 1:
                if indices[0] == 1 or indices[0] == 10:
                    count += 1
                count += 1
            elif len(indices) == 2:
                if indices[0] == 1 and indices[1] == 10:
                    count += 2
                elif all((i not in indices for i in [2, 3, 4, 5])) or all((i not in indices for i in [4, 5, 6, 7])) or all((i not in indices for i in [6, 7, 8, 9])):
                    count += 1
            elif len(indices) <= 6:
                if all((i not in indices for i in [2, 3, 4, 5])) or all((i not in indices for i in [4, 5, 6, 7])) or all((i not in indices for i in [6, 7, 8, 9])):
                    count += 1
            row_start = row_end
            next_row = reservedSeats[row_start][0] if row_start < len(reservedSeats) else n + 1
            count += 2 * (next_row - reservedSeats[row_end - 1][0] - 1)
        return count
