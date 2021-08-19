# class Solution:
#     def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
#         n = N
#         currCells = cells[:]
#         while n > 0:
#             for i in range(len(cells)):
#                 if i == 0 or i == len(cells)-1:
#                     currCells[i] = 0
#                 elif cells[i-1] == cells[i+1]:
#                     currCells[i] = 1
#                 else:
#                     currCells[i] = 0
#             cells = currCells[:]
#             n -= 1
#         return cells

class Solution:
    def prisonAfterNDays(self, cells, N):

        seen = {}
        while N:
            seen.setdefault(str(cells), N)
            print(seen)
            N -= 1
            cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
            if str(cells) in seen:
                N %= seen[str(cells)] - N
        return cells
