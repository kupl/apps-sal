import collections


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        last_blast = collections.defaultdict(lambda: 0)
        visited = set()

        def getN(i, j):
            direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            for diff in direction:
                i_diff, j_diff = diff
                curr_i = i + i_diff
                curr_j = j + j_diff
                if curr_i < 0 or curr_j < 0 or curr_i >= len(grid) or curr_j >= len(grid[0]):
                    continue
                yield [curr_i, curr_j]

        node_to_trav = deque()
        node_to_trav.append((0, 0, k))

        min_steps = -1

        while node_to_trav:
            trav_length = len(node_to_trav)
            min_steps += 1
            for i in range(trav_length):
                curr_node = node_to_trav.popleft()
                i, j, r_dyno = curr_node
                visited.add((i, j))
                if i == len(grid) - 1 and j == len(grid[0]) - 1:
                    return min_steps
                for n in getN(i, j):
                    n_i, n_j = n

                    if grid[n_i][n_j] == 0:
                        if (n_i, n_j, r_dyno) not in visited:
                            node_to_trav.append((n_i, n_j, r_dyno))
                            visited.add((n_i, n_j, r_dyno))
                    elif r_dyno > last_blast[(n_i, n_j)]:
                        if (n_i, n_j, r_dyno - 1) not in visited:
                            node_to_trav.append((n_i, n_j, r_dyno - 1))
                            last_blast[(n_i, n_j)] = r_dyno - 1
                            visited.add((n_i, n_j, r_dyno - 1))

        return -1
