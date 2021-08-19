class Solution:

    def countAvailableSeats(self, row, taken_slots):
        if row not in taken_slots:
            return 2
        if not taken_slots[row][0] and (not taken_slots[row][1]) and (not taken_slots[row][2]) and (not taken_slots[row][3]):
            return 2
        elif not taken_slots[row][0] and (not taken_slots[row][1]):
            return 1
        elif not taken_slots[row][1] and (not taken_slots[row][2]):
            return 1
        elif not taken_slots[row][2] and (not taken_slots[row][3]):
            return 1
        del taken_slots[row]
        return 0

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedSeats.sort(key=lambda s: s[0])
        (res, prev_row) = (0, 1)
        taken_slots = collections.defaultdict(lambda: [False, False, False, False])
        for (row, col) in reservedSeats:
            if prev_row != row:
                res += 2 * (row - prev_row - 1)
                res += self.countAvailableSeats(prev_row, taken_slots)
            if col in (2, 3):
                taken_slots[row][0] = True
            elif col in (4, 5):
                taken_slots[row][1] = True
            elif col in (6, 7):
                taken_slots[row][2] = True
            elif col in (8, 9):
                taken_slots[row][3] = True
            prev_row = row
        res += 2 * (n - prev_row)
        res += self.countAvailableSeats(prev_row, taken_slots)
        return res
