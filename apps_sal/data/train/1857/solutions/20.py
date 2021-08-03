class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        res = 0
        d = dict()
        for seat in reservedSeats:
            if seat[0] in d:
                d[seat[0]].append(seat[1])
            else:
                d[seat[0]] = [seat[1]]

        row = 1
        for k in sorted(d):
            if row < k:
                res += (k - row) * 2
                row = k + 1
            elif row == k:
                row += 1

            centre_occ = False
            if not any(s in d[k] for s in (2, 3, 4, 5)):
                res += 1
                centre_occ = True
            if not any(s in d[k] for s in (6, 7, 8, 9)):
                res += 1
                centre_occ = True

            if not centre_occ and not any(s in d[k] for s in (4, 5, 6, 7)):
                res += 1

        if row <= n:
            res += (n + 1 - row) * 2
        return res
