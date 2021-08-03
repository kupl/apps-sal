import heapq


class Knight:
    def __init__(self, start, size):
        self.i, self.j = start
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.moves = [(2, 1), (2, -1), (1, -2), (1, 2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]

    def valid(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size and not self.board[x][y]

    def find_neighbour(self, x, y):
        heap = []
        for i, j in self.moves:
            ni, nj = x + i, y + j
            if self.valid(ni, nj):
                neighbours = self.find_neighbour_of_neighbour(ni, nj)
                heapq.heappush(heap, (neighbours, (i, j)))
        return heap

    def find_neighbour_of_neighbour(self, x, y):
        return sum(self.valid(x + i, y + j) for i, j in self.moves)

    def get_path(self):
        i, j = self.i, self.j
        path = [(i, j)]
        for n in range(self.size * self.size):
            self.board[i][j] = n + 1
            avl = self.find_neighbour(i, j)
            if not avl:
                break
            _, (ni, nj) = heapq.heappop(avl)
            i += ni
            j += nj
            path.append((i, j))
        return path


def knights_tour(start, size):
    return Knight(start, size).get_path()
