from collections import deque

def pac_man(N, PM, enemies):
    grid = [[2] * N for i in range(N)]
    for enemy in enemies:
        for i in range(N):
            grid[enemy[0]][i] = "E"
        for j in range(N):
            grid[j][enemy[1]] = "E"
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    queue, ans = deque([tuple(PM)]), 0
    visited = set()
    while queue:
        node = queue.popleft()
        for dirc in directions:
            new_pos = (node[0] + dirc[0], node[1] + dirc[1])
            if 0 <= new_pos[0] < N and 0 <= new_pos[1] < N:
                if grid[new_pos[0]][new_pos[1]] == 2:
                    if new_pos not in visited:
                        ans += 1
                        visited.add(new_pos)
                        queue.append(tuple(new_pos))
    return ans - 1 if ans > 0 else 0
