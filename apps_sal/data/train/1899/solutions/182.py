class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        '''
        1111
        1001
        0000
        1000
        1110
        '''

        i1, i2 = self.find_islands(A)

        for (x, y, n) in self.enlarge(i1):
            if (x, y) in i2:
                return n

    def find_islands(self, A: List[List[int]]) -> List[Set[Tuple[int, int]]]:
        visited = set()
        islands = []
        for x, ys in enumerate(A):
            for y, c in enumerate(ys):
                if (x, y) not in visited and c == 1:
                    to_visit = [(x, y)]
                    island = set()
                    while to_visit:
                        cx, cy = to_visit.pop(0)
                        if (cx, cy) in visited:
                            continue
                        visited.add((cx, cy))
                        island.add((cx, cy))
                        for (ax, ay) in self.adjacent((cx, cy)):
                            if ax >= 0 and ay >= 0 and ax < len(A) and ay < len(A[ax]) and A[ax][ay] == 1:
                                to_visit.append((ax, ay))
                    islands.append(island)
        return islands

    def enlarge(self, island: Set[Tuple[int, int]]) -> Generator[Tuple[int, int, int], None, None]:
        visited = set()
        to_visit = []
        for x, y in island:
            visited.add((x, y))
            for ax, ay in self.adjacent((x, y)):
                visited.add((x, y))
                if (ax, ay) not in island:
                    to_visit.append((ax, ay, 0))
        while to_visit:
            x, y, n = to_visit.pop(0)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for ax, ay in self.adjacent((x, y)):
                if (ax, ay) in visited:
                    continue
                to_visit.append((ax, ay, n + 1))
            yield x, y, n

    def adjacent(self, cell: Tuple[int, int]) -> List[Tuple[int, int]]:
        return [(cell[0] + x, cell[1] + y) for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
