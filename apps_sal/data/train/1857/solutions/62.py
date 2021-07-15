class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        \"\"\"
        Runtime: O(m) where m is length of reservedSeats, Space: O(m)
        \"\"\"
        reserved = dict()
        for seat in reservedSeats:
            row, col = seat
            if row not in reserved:
                reserved[row] = {col}
            else:
                reserved[row].add(col)
        
        groups = 2 * n
        for _, cols in reserved.items():
            sections = 0
            if not any(col in cols for col in (2, 3, 4, 5)):
                sections += 1
            if not any(col in cols for col in (6, 7, 8, 9)):
                sections += 1
            # check if sections == 0 to avoid double counting where the sections overlap
            if sections == 0 and not any(col in cols for col in (4, 5, 6, 7)):
                sections += 1
            groups += sections - 2
        return groups
        
