class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        def isOpen(row, seat):
            for i in range(seat, seat + 4):
                if i in grid[row]:
                    return False
            return True

        def isClosed(row, seat):
            return not isOpen(row, seat)

        grid = {}

        for row, seat in reservedSeats:
            if row not in grid:
                grid[row] = {}
            grid[row][seat] = True

        result = n * 2
        for i in grid:
            left = isOpen(i, 2)
            middle = isOpen(i, 4)
            right = isOpen(i, 6)

            if middle:
                if left and right:
                    pass
                else:
                    result -= 1
            else:
                if not left:
                    result -= 1
                if not right:
                    result -= 1

        return result
