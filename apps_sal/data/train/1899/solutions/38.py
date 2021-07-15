import queue

def findIsland(map, color):
    res = [0, 0]
    for row, line in enumerate(map):
        for col, n in enumerate(line):
            if n == color:
                return [row, col]
    return res


def bfs(row, col, map, rows, cols, find_color, color):
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    visited = [[False for col in range(len(map[0]))] for row in range(len(map))]
    boundry = queue.Queue()
    q = queue.Queue()
    q.put((row, col))
    while not q.empty():
        r, c = q.get()
        # print(\"(\", r, c, \")\", q.qsize())
        if map[r][c] == find_color:
            map[r][c] = color
        for d in delta:
            new_row = r + d[0]
            new_col = c + d[1]
            if new_row < 0 or new_col < 0 or new_row >= rows or new_col >= cols:
                continue
            if map[new_row][new_col] == 0:
                boundry.put((new_row, new_col, 1))
            if map[new_row][new_col] != find_color:
                continue
            if visited[new_row][new_col]:
                continue
            visited[new_row][new_col] = True
            q.put((new_row, new_col))

    return boundry
    # for r, c in boundry:
    #     map[r][c] = 1
            # print(\"(\", new_row, new_col, \")\", end=\" - \", flush=True)
        # print()

def bfs2(q, map, rows, cols, find_color):
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    visited = [[False for col in range(len(map[0]))] for row in range(len(map))]
    # q.put((row, col))
    color = 1
    while not q.empty():
        r, c, col = q.get()
        map[r][c] = col
        for d in delta:
            new_row = r + d[0]
            new_col = c + d[1]
            if new_row < 0 or new_col < 0 or new_row >= rows or new_col >= cols:
                continue
            if map[new_row][new_col] == 'Y':
                return col
            if visited[new_row][new_col]:
                continue
            if map[new_row][new_col] != find_color:
                continue
            else:
                q.put((new_row, new_col, col+1))
            visited[new_row][new_col] = True

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        pos = findIsland(A, 1)
        # print(pos)
        boundry1 = bfs(pos[0], pos[1], A, len(A), len(A[0]), 1, \"X\")
        pos = findIsland(A, 1)
        # print(pos)
        boundry2 = bfs(pos[0], pos[1], A, len(A), len(A[0]), 1, \"Y\")
        dist = bfs2(boundry1, A, len(A), len(A[0]), 0)
        # for line in A:
        #     for char in line:
        #         print(str(char),' ',  end=\"\")
        #     print(flush=True)
        print(dist)
        return dist
