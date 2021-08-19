from collections import namedtuple
import heapq


def shallowest_path(river):
    rows = len(river)
    if rows == 0:
        return []
    cols = len(river[0])
    if cols == 0:
        return []

    Solution = namedtuple('Solution', ['depth', 'path'])
    State = namedtuple('State', ['depth', 'path_length', 'path'])

    best_solution = None
    left_bank_q = [(river[row][0], row, 0) for row in range(rows)]
    heapq.heapify(left_bank_q)

    while left_bank_q:
        visited = set()
        initial_depth, row, col = heapq.heappop(left_bank_q)
        walk_q = [State(depth=initial_depth, path_length=1, path=[(row, col)])]
        while walk_q:
            depth, path_length, path = heapq.heappop(walk_q)
            current_row, current_col = path[-1]
            if (current_row, current_col) in visited or (current_col == 0 and path_length > 1):
                continue
            if current_col == cols - 1:  # We reached the right bank
                if depth == 1 and len(path) == cols:
                    return path  # Optimal path
                if best_solution is None or depth < best_solution.depth or (depth == best_solution.depth and len(path) < len(best_solution.path)):
                    best_solution = Solution(depth, path)
                continue
            visited.add((current_row, current_col))
            best_depth = float('inf') if best_solution is None else best_solution.depth
            for row, col in neighbours(river, current_row, current_col):
                if (row, col) not in visited and river[row][col] <= best_depth:
                    heapq.heappush(walk_q, State(depth=max(depth, river[row][col]), path_length=path_length + 1, path=path + [(row, col)]))

    return best_solution.path


def neighbours(river, row, col):
    rows = len(river)
    cols = len(river[0])

    return ((row + drow, col + dcol)
            for drow in [-1, 0, 1]
            for dcol in [-1, 0, 1]
            if drow != 0 or dcol != 0
            if 0 <= row + drow < rows
            if 0 <= col + dcol < cols)
