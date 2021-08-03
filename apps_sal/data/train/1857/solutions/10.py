class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}
        for r, c in reservedSeats:
            if r not in rows:
                rows[r] = 0
            rows[r] ^= (1 << c)
        res = 0
        p0 = (1 << 2) ^ (1 << 3) ^ (1 << 4) ^ (1 << 5)
        p1 = (1 << 6) ^ (1 << 7) ^ (1 << 8) ^ (1 << 9)
        p2 = (1 << 4) ^ (1 << 5) ^ (1 << 6) ^ (1 << 7)
        for r in rows:
            f0 = (rows[r] & p0) == 0
            f1 = (rows[r] & p1) == 0
            f2 = (rows[r] & p2) == 0
            if f0 and f1:
                res += 2
            elif f0 or f1 or f2:
                res += 1
        return (n - len(rows)) * 2 + res
