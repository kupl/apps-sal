class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        # i,j,k
        # memo = {}

        H = len(grid)
        W = len(grid[0])
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def possible(i, j):
            res = []
            for add in direction:
                i_, j_ = i + add[0], j + add[1]
                if 0 <= i_ and i_ < H and 0 <= j_ and j_ < W:
                    res.append([i_, j_])

            return res

        queue = [(0, 0, k)]
        step = 0
        q = 0
        K = k

        # i,j,k
        visited = {}
        visited[(0, 0)] = k

        if (0, 0) == (H - 1, W - 1):
            return step

        while len(queue) > q:
            step += 1
            size = len(queue) - q
            for _ in range(size):
                i, j, k = queue[q]
                q += 1

                for i_, j_ in possible(i, j):
                    if grid[i_][j_] == 0:
                        if (i_, j_) not in visited or visited[(i_, j_)] < k:
                            queue.append((i_, j_, k))
                            visited[(i_, j_)] = k
                            if i_ == H - 1 and j_ == W - 1:
                                return step
                    else:
                        if k - 1 >= 0:
                            if (i_, j_) not in visited or visited[(i_, j_)] < k - 1:
                                queue.append((i_, j_, k - 1))
                                visited[(i_, j_)] = k - 1
                                if i_ == H - 1 and j_ == W - 1:
                                    return step

        return -1
