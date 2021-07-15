from typing import List, Tuple


class Game(List[List[bool]]):
    def __init__(self, cells: List[List[int or bool]]) -> None:
        if not cells[0]:
            self.height = self.width = 2
            self[0:2] = [[False, False], [False, False]]
            return

        self.height: int = len(cells)
        self.width: int = len(cells[0])

        for i in range(len(cells)):
            row = []
            for val in cells[i]:
                row.append(bool(val))
            self.append(row)
        self.__trim()

    def __trim(self) -> None:
        for _ in range(self.height):
            row = self[0]
            if True in row:
                break
            del self[0]
            self.height -= 1

        for _ in reversed(list(range(self.height))):
            row = self[-1]
            if True in row:
                break
            del self[-1]
            self.height -= 1

        empty = True
        while empty:
            for row in self:
                if row[0]:
                    empty = False
                    break
            else:
                for row in self:
                    del row[0]
                self.width -= 1

        empty = True
        while empty:
            for row in self:
                if row[-1]:
                    empty = False
                    break
            else:
                for row in self:
                    del row[-1]
                self.width -= 1

    def __pad(self) -> None:
        self.width += 2
        self.height += 2

        for i in self:
            i.insert(0, False)
            i.append(False)
        self.insert(0, [False] * self.width)
        self.append([False] * self.width)

    def __neighbors(self, i: int, j: int):
        north = i == 0
        west = j == 0
        south = i == self.height - 1
        east = j == self.width - 1

        return int(
            (self[i - 1][j - 1] if not north and not west else 0)
            + (self[i - 1][j] if not north else 0)
            + (self[i - 1][j + 1] if not north and not east else 0)
            + (self[i][j - 1] if not west else 0)
            + (self[i][j + 1] if not east else 0)
            + (self[i + 1][j - 1] if not south and not west else 0)
            + (self[i + 1][j] if not south else 0)
            + (self[i + 1][j + 1] if not south and not east else 0)
        )

    def iterate(self):
        self.__pad()

        queue: List[Tuple[int, int]] = []
        for i in range(self.height):
            for j in range(self.width):
                status = self[i][j]
                neighbors = self.__neighbors(i, j)
                if (status and (neighbors < 2 or neighbors > 3)) or (
                    not status and (neighbors == 3)
                ):
                    queue.append((i, j))

        for i, j in queue:
            self[i][j] = not self[i][j]

        self.__trim()

    def export(self) -> List[List[int]]:
        if not self.height or not self.width:
            return [[]]

        out: List[List[int]] = []
        for i in self:
            row = []
            for j in i:
                row.append(int(j))
            out.append(row)
        return out


def get_generation(cells: List[List[str]], generations):
    board = Game(cells)

    for _ in range(generations):
        board.iterate()

    return board.export()


