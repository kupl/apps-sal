class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        if len(A) == 0:
            return -1

        rows = len(A)
        columns = len(A[0])
        seen = dict()

        # identify the components
        def dfs(row, column):
            island = set()
            border = set()
            to_visit = [(row, column)]
            while len(to_visit) > 0:
                r, c = to_visit.pop()
                if r < 0 or r >= rows or c < 0 or c >= columns or (r, c) in seen or A[r][c] != 1:
                    continue

                seen[(r, c)] = island
                island.add((r, c))
                if (r > 0 and A[r - 1][c] == 0) or \\
                    (r < rows - 1 and A[r + 1][c] == 0) or \\
                    (c > 0 and A[r][c - 1] == 0) or \\
                    (c < columns - 1 and A[r][c + 1] == 0):
                    border.add((r, c))

                to_visit.append((r - 1, c))
                to_visit.append((r, c - 1))
                to_visit.append((r + 1, c))
                to_visit.append((r, c + 1))

            return island, border


        borders = []
        for row in range(rows):
            for column in range(columns):
                if A[row][column] != 1 or (row, column) in seen:
                    continue

                island, border = dfs(row, column)
                borders.append(border)

        assert len(borders) == 2

        min_distance = rows + columns
        for r1, c1 in borders[0]:
            for r2, c2 in borders[1]:
                min_distance = min(min_distance, abs(r1 - r2) + abs(c1 - c2) - 1)

        return min_distance
