class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:

        n = len(grid)
        q = [((0, 1), (0, 0))]
        visited = set(q)
        step = 0
        while q:
            l = len(q)
            for _ in range(l):
                (head, tail) = q.pop(0)
                if head == (n - 1, n - 1) and tail == (n - 1, n - 2):
                    return step
                if head[1] > tail[1]:

                    if head[1] + 1 < n and grid[head[0]][head[1] + 1] == 0 and not ((head[0], head[1] + 1), (tail[0], tail[1] + 1)) in visited:
                        q.append(((head[0], head[1] + 1), (tail[0], tail[1] + 1)))
                        visited.add(((head[0], head[1] + 1), (tail[0], tail[1] + 1)))
                    if head[0] + 1 < n and grid[head[0] + 1][head[1]] + grid[tail[0] + 1][tail[1]] == 0:
                        if not ((head[0] + 1, head[1]), (tail[0] + 1, tail[1])) in visited:
                            q.append(((head[0] + 1, head[1]), (tail[0] + 1, tail[1])))
                            visited.add(((head[0] + 1, head[1]), (tail[0] + 1, tail[1])))
                        if not ((head[0] + 1, head[1] - 1), tail) in visited:
                            q.append(((head[0] + 1, head[1] - 1), tail))
                            visited.add(((head[0] + 1, head[1] - 1), tail))

                else:

                    if head[0] + 1 < n and grid[head[0] + 1][head[1]] == 0 and not ((head[0] + 1, head[1]), (tail[0] + 1, tail[1])) in visited:
                        q.append(((head[0] + 1, head[1]), (tail[0] + 1, tail[1])))
                        visited.add(((head[0] + 1, head[1]), (tail[0] + 1, tail[1])))
                    if head[1] + 1 < n and grid[head[0]][head[1] + 1] + grid[tail[0]][tail[1] + 1] == 0:
                        if not ((head[0], head[1] + 1), (tail[0], tail[1] + 1)) in visited:
                            q.append(((head[0], head[1] + 1), (tail[0], tail[1] + 1)))
                            visited.add(((head[0], head[1] + 1), (tail[0], tail[1] + 1)))
                        if not ((head[0] - 1, head[1] + 1), tail) in visited:
                            q.append(((head[0] - 1, head[1] + 1), tail))
                            visited.add(((head[0] - 1, head[1] + 1), tail))
            step += 1

        return -1
