class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        if not reservedSeats:
            return 2 * n

        row_reservations = dict()

        for reservation in reservedSeats:

            row = reservation[0]
            seat = reservation[1]

            if seat == 1 or seat == 10:
                continue

            if row not in row_reservations:
                row_reservations[row] = {seat}
            else:
                row_reservations[row].add(seat)

        total_families = 2 * (n - len(row_reservations))

        def lesser_two_fam(rev_res):

            fam_count = 0

            for row in list(rev_res.values()):
                pos1 = 1
                pos2 = 1
                pos3 = 1

                if 2 in row or 3 in row:
                    pos1 = 0
                if 4 in row or 5 in row:
                    pos1 = 0
                    pos2 = 0
                if 6 in row or 7 in row:
                    pos2 = 0
                    pos3 = 0
                if 8 in row or 9 in row:
                    pos3 = 0

                fam_count += max(pos1, pos2, pos3)

            return fam_count
        total_families += lesser_two_fam(row_reservations)

        return total_families
