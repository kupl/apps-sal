from typing import List


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        if not A or not A[0]:
            return 0
        # closest distance between two 1s from different groups
        h, w = len(A), len(A[0])

        def _get_island():
            \"\"\"Return border of current island\"\"\"
            island = set()
            border = set()
            idx_i = 0
            idx_j = 0
            for i in range(h):
                for j in range(w):
                    if A[i][j] == 1:
                        # find an 1
                        idx_i, idx_j = i, j
                        break
            # BFS
            island.add((idx_i, idx_j))
            queue = [(idx_i, idx_j)]
            while queue:
                i, j = queue.pop()
                # only keep border
                # if at vertical border
                if i > 0 and A[i - 1][j] == 1 and j > 0 and A[i][j - 1] == 1 \\
                        and i < h - 1 and A[i + 1][j] == 1 and j < w - 1 and A[i][j + 1] == 1:
                    # not at border
                    pass
                else:
                    border.add((i, j))
                nxts = set()
                if i > 0:
                    nxts.add((i - 1, j))
                if j > 0:
                    nxts.add((i, j - 1))
                if i < h - 1:
                    nxts.add((i + 1, j))
                if j < w - 1:
                    nxts.add((i, j + 1))
                for nxt in nxts:
                    if A[nxt[0]][nxt[1]] == 1 and nxt not in island:
                        island.add(nxt)
                        queue.append(nxt)

            # change current island to 0
            for i, j in island:
                A[i][j] = 0
            return border

        island_1 = _get_island()
        island_2 = _get_island()
        res = h + w
        for i1 in island_1:
            for i2 in island_2:
                res = min(res, abs(i1[0] - i2[0]) + abs(i1[1] - i2[1]) - 1)
        return res


