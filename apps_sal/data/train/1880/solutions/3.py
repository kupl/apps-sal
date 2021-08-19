class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        def transform(cells):
            nxtCells = [0] * len(cells)
            for i in range(1, len(cells) - 1):
                nxtCells[i] = 1 if cells[i - 1] == cells[i + 1] else 0
            return nxtCells

        day = 0
        while N > 0:
            cells = transform(cells)
            day += 1
            N -= 1
            if day == 1:
                origin = [i for i in cells]
            elif cells == origin:
                # print(day, N, cells)
                N %= day - 1
                # print(day, N, cells)

            # print(N, cells)

        return cells
