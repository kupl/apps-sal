class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def nextDay(cells):
            ans = [0] #start
            for i in range(1, len(cells) - 1):
                ans.append(int(cells[i - 1] == cells[i + 1]))
            ans.append(0)
            return ans
        
        seen = {}
        forwarded = False
        
        while N > 0: # when there is loop left
            if not forwarded: # if cycle hasn't been detected
                snapshot = tuple(cells)
                if snapshot in seen: # detected cycle
                    N %= seen[snapshot] - N # length of cycle
                    forwarded = True
                else:
                    seen[snapshot] = N
            if N > 0: # update snapshot to next day's
                N -= 1
                cells = nextDay(cells)
        return cells
        
    # Given K number of cells, there could be at most 2**K possible states. If the number of steps is larger than all possible states (N > 2 ** K), we are destined to repeat ourselves sooner or later.

