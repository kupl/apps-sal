class Solution:

    def shortestBridge(self, A: List[List[int]]) -> int:
        (R, C) = (len(A), len(A[0]))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col, group):
            A[row][col] = marker
            group.append((row, col))
            for (dr, dc) in directions:
                (new_row, new_col) = (row + dr, col + dc)
                if 0 <= new_row < R and 0 <= new_col < C and (A[new_row][new_col] == 1):
                    dfs(new_row, new_col, group)
            return group
        (groups, marker) = ([], 2)
        for r in range(R):
            for c in range(C):
                if A[r][c] == 1:
                    groups.append((dfs(r, c, []), marker))
                    marker += 1
        groups = sorted(groups, key=lambda x: len(x[0]))
        (src_group, src_marker) = groups[0]
        q = deque([(row, col, 0) for (row, col) in src_group])
        target = set(groups[1][0])
        while q:
            (row, col, curr_distance) = q.pop()
            if (row, col) in target:
                return curr_distance - 1
            for (dr, dc) in directions:
                (new_row, new_col) = (row + dr, col + dc)
                if 0 <= new_row < R and 0 <= new_col < C and (A[new_row][new_col] != src_marker):
                    q.appendleft((new_row, new_col, curr_distance + 1))
                    A[new_row][new_col] = src_marker
        return -1
