class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        orientation = 'h'
        head, tail = (0, 1), (0, 0)
        q = collections.deque()
        q.append((head, tail, orientation))
        visited = set()
        visited.add((head, tail, orientation))
        moves = 0
        n = len(grid)
        target_head, target_tail = (n - 1, n - 1), (n - 1, n - 2)

        while q:
            for _ in range(len(q)):
                head, tail, orientation = q.popleft()
                if head == target_head and tail == target_tail:
                    return moves
                head_x, head_y = head
                tail_x, tail_y = tail
                if orientation == 'h':
                    if head_y + 1 < n and grid[head_x][head_y + 1] == 0:
                        node = ((head_x, head_y + 1), head, orientation)
                        if node not in visited:
                            q.append(node)
                            visited.add(node)
                    if head_x + 1 < n and grid[head_x + 1][head_y] == 0 and grid[tail_x + 1][tail_y] == 0:
                        node = ((head_x + 1, head_y), (tail_x + 1, tail_y), orientation)
                        if node not in visited:
                            q.append(node)
                            visited.add(node)
                    if head_x + 1 < n and grid[head_x + 1][head_y] == 0 and grid[head_x + 1][tail_y] == 0:
                        node = ((tail_x + 1, tail_y), tail, 'v')
                        if node not in visited:
                            q.append(node)
                            visited.add(node)

                else:
                    if head_y + 1 < n and grid[head_x][head_y + 1] == 0 and grid[tail_x][tail_y + 1] == 0:
                        node = ((head_x, head_y + 1), (tail_x, tail_y + 1), 'v')
                        if node not in visited:
                            q.append(node)
                            visited.add(node)
                    if head_x + 1 < n and grid[head_x + 1][head_y] == 0:
                        node = ((head_x + 1, head_y), head, 'v')
                        if node not in visited:
                            q.append(node)
                            visited.add(node)
                    if head_y + 1 < n and grid[head_x][head_y + 1] == 0 and grid[tail_x][tail_y + 1] == 0:
                        node = ((tail_x, tail_y + 1), tail, 'h')
                        if node not in visited:
                            q.append(node)
                            visited.add(node)
            moves += 1

        return -1
