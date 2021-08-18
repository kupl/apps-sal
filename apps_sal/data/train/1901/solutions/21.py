class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        N, M = len(grid), len(grid[0])
        visited = [[0] * M for _ in range(N)]
        group_ids_ = collections.defaultdict()
        group_counts_ = collections.Counter()
        _id_ = 0
        previous_count = 0
        for row in range(N):
            for col in range(M):
                if grid[row][col] == 1 and visited[row][col] == 0:
                    _id_ += 1
                    visited[row][col] = 1
                    stack = [(row, col)]
                    group_ids_[(row, col)] = _id_
                    while stack:
                        r, c = stack.pop()
                        for newr, newc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                            if 0 <= newr < N and 0 <= newc < M and visited[newr][newc] == 0 and grid[newr][newc] == 1:
                                visited[newr][newc] = 1
                                stack.append((newr, newc))
                                group_ids_[(newr, newc)] = _id_

                    group_counts_[_id_] = sum([sum(l) for l in visited]) - previous_count
                    previous_count = sum([sum(l) for l in visited])

        biggest = 0
        hasZero = False
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 0:
                    hasZero = True
                    groups = set()
                    for newr, newc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                        if 0 <= newr < N and 0 <= newc < M and grid[newr][newc] == 1:
                            groups.add(group_ids_[(newr, newc)])
                    biggest = max(biggest, sum([group_counts_[_id_] for _id_ in groups]) + 1)
        if hasZero:
            return biggest
        else:
            return N * M
