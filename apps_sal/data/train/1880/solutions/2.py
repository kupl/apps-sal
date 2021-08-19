class Solution:

    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        def nextDay(cells):
            ans = [0]
            for i in range(1, len(cells) - 1):
                ans.append(int(cells[i - 1] == cells[i + 1]))
            ans.append(0)
            return ans
        seen = {}
        forwarded = False
        while N > 0:
            if not forwarded:
                snapshot = tuple(cells)
                if snapshot in seen:
                    N %= seen[snapshot] - N
                    forwarded = True
                else:
                    seen[snapshot] = N
            if N > 0:
                N -= 1
                cells = nextDay(cells)
        return cells
