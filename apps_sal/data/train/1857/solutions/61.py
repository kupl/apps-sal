from itertools import groupby
from re import finditer

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        ans = 2*n
        reservedSeats.sort()
        rows = groupby(reservedSeats, key=lambda x: x[0])
        for r, c in rows:
            row = ['O']*10
            for _, col in c:
                row[col-1] = 'X'
            row = ''.join(row)
            idx = {f.start() for f in finditer('(?=OOOO)', row)}
            if not idx:
                ans -= 2
            elif 1 in idx and 5 in idx:
                continue
            elif 1 in idx or 3 in idx or 5 in idx:
                ans -= 1
            else:
                ans -= 2
        return ans
    \"\"\"
    OOO OOOO OOO
    OOO OOOO OOO
    \"\"\"
