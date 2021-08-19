class Solution:

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = defaultdict(set)
        if len(reservedSeats) == 0:
            return 2 * n
        for seat in reservedSeats:
            (row, col) = seat
            seats[row].add(col)
        result = 0
        for i in seats.keys():
            total = 0
            if len({2, 3, 4, 5}.intersection(seats[i])) == 0:
                total += 1
            if len({6, 7, 8, 9}.intersection(seats[i])) == 0:
                total += 1
            if len({4, 5, 6, 7}.intersection(seats[i])) == 0 and total == 0:
                total += 1
            result += total
        rowsLeft = n - len(seats)
        result += 2 * rowsLeft
        return result
