class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        from collections import defaultdict
        taken_seats = defaultdict(int)
        for row, col in reservedSeats:
            taken_seats[row] = taken_seats[row] | (1 << (col - 1))
        res = 0
        for seat in taken_seats.values():
            cnt = 0
            if (seat & int('0111100000', 2)) == 0:
                cnt += 1
            if (seat & int('0000011110', 2)) == 0:
                cnt += 1
            # cnt==0 means 2345 and 4567 is not taken respectively
            # and
            if (seat & int('0001111000', 2)) == 0 and cnt == 0:
                cnt = 1
            res += cnt
        return 2 * (n - len(taken_seats)) + res
