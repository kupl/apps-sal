class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        prison_size = len(cells)
        seen = {}
        seen[str(cells)] = 0
        history = [cells]

        for d in range(1, N + 1):
            ans = [0] * prison_size
            for i in range(1, 7):
                ans[i] = 1 if cells[i - 1] == cells[i + 1] else 0

            if str(ans) in seen:
                cycle_length = d - seen[str(ans)]
                return history[seen[str(ans)] + (N - d) % cycle_length]
            else:
                history.append(ans)
                seen[str(ans)] = d
            cells = ans

        return cells
