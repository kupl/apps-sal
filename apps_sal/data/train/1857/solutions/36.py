class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = set()
        rows = set()
        for row, col in reservedSeats:
            reserved.add((row, col))
            rows.add(row)
        count = 2 * (n - len(rows))
        for row in rows:
            for col in [2, 4, 6]:
                if (row, col) not in reserved and (row, col + 1) not in reserved and (row, col + 2) not in reserved and (row, col + 3) not in reserved:
                    reserved.add((row, col))
                    reserved.add((row, col + 1))
                    reserved.add((row, col + 2))
                    reserved.add((row, col + 3))
                    count += 1
        return count
