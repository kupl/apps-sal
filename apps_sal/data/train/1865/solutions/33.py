class Solution:

    def minPushBox(self, grid: List[List[str]]) -> int:

        def player_moves(box_i, box_j, p_i, p_j):
            res = []
            if p_i > 0 and grid[p_i - 1][p_j] != '#' and ((p_i - 1, p_j) != (box_i, box_j)):
                res.append((p_i - 1, p_j))
            if p_i < len(grid) - 1 and grid[p_i + 1][p_j] != '#' and ((p_i + 1, p_j) != (box_i, box_j)):
                res.append((p_i + 1, p_j))
            if p_j > 0 and grid[p_i][p_j - 1] != '#' and ((p_i, p_j - 1) != (box_i, box_j)):
                res.append((p_i, p_j - 1))
            if p_j < len(grid[0]) - 1 and grid[p_i][p_j + 1] != '#' and ((p_i, p_j + 1) != (box_i, box_j)):
                res.append((p_i, p_j + 1))
            return res

        def is_accessible(cell_i, cell_j, box_i, box_j, p_i, p_j):
            if grid[cell_i][cell_j] == '#':
                return False
            q = deque()
            visited = set()
            q.append((p_i, p_j))
            visited.add((p_i, p_j))
            while q:
                size = len(q)
                for i in range(size):
                    pop = q.popleft()
                    if pop == (cell_i, cell_j):
                        return True
                    for nex in player_moves(box_i, box_j, pop[0], pop[1]):
                        if nex not in visited:
                            q.append(nex)
                            visited.add(nex)
            return False

        def box_moves(state):
            res = set()
            (box_i, box_j, p_i, p_j) = (state[0], state[1], state[2], state[3])
            if box_i > 0 and is_accessible(box_i - 1, box_j, box_i, box_j, p_i, p_j) and (box_i + 1 < len(grid)) and (grid[box_i + 1][box_j] != '#'):
                res.add((box_i + 1, box_j, box_i, box_j))
            if box_i < len(grid) - 1 and is_accessible(box_i + 1, box_j, box_i, box_j, p_i, p_j) and (box_i - 1 >= 0) and (grid[box_i - 1][box_j] != '#'):
                res.add((box_i - 1, box_j, box_i, box_j))
            if box_j > 0 and is_accessible(box_i, box_j - 1, box_i, box_j, p_i, p_j) and (box_j + 1 < len(grid[0])) and (grid[box_i][box_j + 1] != '#'):
                res.add((box_i, box_j + 1, box_i, box_j))
            if box_j < len(grid[0]) - 1 and is_accessible(box_i, box_j + 1, box_i, box_j, p_i, p_j) and (box_j - 1 >= 0) and (grid[box_i][box_j - 1] != '#'):
                res.add((box_i, box_j - 1, box_i, box_j))
            return res

        def start_state():
            (box_i, box_j, p_i, p_j) = (-1, -1, -1, -1)
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 'B':
                        (box_i, box_j) = (i, j)
                    elif grid[i][j] == 'S':
                        (p_i, p_j) = (i, j)
            return (box_i, box_j, p_i, p_j)
        q = deque()
        visited = set()
        start = start_state()
        q.append(start)
        visited.add(start)
        moves = -1
        while q:
            size = len(q)
            moves += 1
            for i in range(size):
                pop = q.popleft()
                if grid[pop[0]][pop[1]] == 'T':
                    return moves
                for nx in box_moves(pop):
                    if nx not in visited:
                        q.append(nx)
                        visited.add(nx)
        return -1
