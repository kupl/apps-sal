class Solution:

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        (left, right, mid) = (set(), set(), set())
        count = 0
        for (row, col) in reservedSeats:
            if row in left and row in right and (row in mid):
                continue
            if col < 6 and col > 1:
                left.add(row)
            if col < 10 and col > 5:
                right.add(row)
            if col < 8 and col > 3:
                mid.add(row)
        for i in left | right | mid:
            if i not in mid:
                count += 1
            elif i not in left or i not in right:
                count += 1
        count += 2 * (n - len(left | right | mid))
        return count
