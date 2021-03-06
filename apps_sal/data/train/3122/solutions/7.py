moves = [[(-2, -1), [(-3, 0), (-1, 0), (0, -3), (0, 1), (-2, -2), (-2, 2), (-1, -1), (1, -1)]], [(-1, -2), [(-3, 0), (1, 0), (0, -3), (0, -1), (-2, -2), (2, -2), (-1, -1), (-1, 1)]], [(1, -2), [(3, 0), (-1, 0), (0, -3), (0, -1), (-2, -2), (2, -2), (1, -1), (1, 1)]], [(2, -1), [(3, 0), (1, 0), (0, -3), (0, 1), (2, -2), (2, 2), (-1, -1), (1, -1)]], [(-2, 1), [(-3, 0), (-1, 0), (0, 3), (0, -1), (-2, -2), (-2, 2), (-1, 1), (1, 1)]], [(-1, 2), [(-3, 0), (1, 0), (0, 3), (0, 1), (-2, 2), (2, 2), (-1, -1), (-1, 1)]], [(1, 2), [(3, 0), (-1, 0), (0, 3), (0, 1), (-2, 2), (2, 2), (1, -1), (1, 1)]], [(2, 1), [(3, 0), (1, 0), (0, 3), (0, -1), (2, -2), (2, 2), (-1, 1), (1, 1)]]]


def chess_triangle(n, m):
    r = 0
    for x in range(n):
        for y in range(m):
            for ((dx, dy), move) in moves:
                if not (0 <= x + dx < n and 0 <= y + dy < m):
                    continue
                for (mx, my) in move:
                    if 0 <= x + mx < n and 0 <= y + my < m:
                        r += 1
    return r
