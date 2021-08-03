class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = collections.defaultdict(lambda: [])
        for row, col in reservedSeats:
            rows[row].append(col)
        ans = (n - len(rows)) * 2

        def solveRow(row, pos, memo):
            if pos >= 7:
                return 0
            elif pos in memo:
                return memo[pos]

            ret = 0
            if pos in (0, 2, 4, 6) or sum(row[pos: pos + 4]) > 0:
                ret = solveRow(row, pos + 1, memo)
            else:
                ret = max(solveRow(row, pos + 1, memo), 1 + solveRow(row, pos + 4, memo))
            memo[pos] = ret
            return ret

        for row_id in rows:
            row = [0] * 10
            for col in rows[row_id]:
                row[col - 1] = 1
            ans += solveRow(row, 0, {})
        return ans
