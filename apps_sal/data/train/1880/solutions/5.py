class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        if not cells:
            return cells

        day1 = self.nextDay(cells)
        cells = day1.copy()
        count = 0
        N -= 1

        while N > 0:
            each_day = self.nextDay(cells)
            count += 1
            N -= 1

            if each_day == day1:
                N = N % count
            cells = each_day
        return cells

    def nextDay(self, cells):
        ret = [0]
        for i in range(1, len(cells) - 1):
            ret.append(int(cells[i - 1] == cells[i + 1]))
        ret.append(0)
        return ret

        return cells
