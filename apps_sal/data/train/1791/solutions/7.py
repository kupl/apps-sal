from collections import deque

B = {'^':'v', 'v':'^', '<':'>', '>':'<'}
L = {'^':'<', 'v':'>', '<':'v', '>':'^'}
R = {'^':'>', 'v':'<', '<':'^', '>':'v'}
F = {'^': lambda i,j: (i-1, j),
     'v': lambda i,j: (i+1, j),
     '<': lambda i,j: (i, j-1),
     '>': lambda i,j: (i, j+1)}

def escape(maze):
    H, W = len(maze), len(maze[0])
    a, b, c = next((a,b,c) for a,row in enumerate(maze) for b,c in enumerate(row) if c in "^<v>")
    left, seen = deque([(a, b, c, [])]), set()
    while left:
        i, j, p, T = left.popleft()
        if i in (0, H-1) or j in (0, W-1): return T
        if (i, j, p) in seen: continue
        seen.add((i, j, p))
        k, l = F[p](i, j)
        if maze[k][l] == ' ': left.append((k, l, p, T + ['F']))
        left.extend([(i, j, L[p], T + ['L']), (i, j, R[p], T + ['R']), (i, j, B[p], T + ['B'])])
    return []
