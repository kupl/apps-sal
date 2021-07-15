def execute(code):
    x, y = 0, 1
    direction = 1
    visited = {(x, y)}
    loops = []
    i = 0
    while i < len(code):
        c = code[i]
        i += 1
        if c == '(':
            j = i
            p = 1
            while p:
                if code[j] == '(': p += 1
                elif code [j] == ')': p -= 1
                j += 1
            k = j
            while k < len(code) and code[k].isdigit(): k += 1
            reps = int(code[j:k]) if k > j else 1
            if reps == 0:
                i = k
                continue
            loops.append((i, reps-1))
        elif c == ')':
            start, reps = loops.pop()
            if reps:
                loops.append((start, reps-1))
                i = start
        elif c not in 'FLR': raise RuntimeError(f'Unknown command: {c}')
        j = i
        while i < len(code) and code[i].isdigit():
            i += 1
        steps = int(code[j:i]) if i > j else 1
        if c == 'F':
            for _ in range(steps):
                x += dx[direction]
                y += dy[direction]
                visited.add((x, y))
        elif c == 'R': direction = (direction + steps) % 4
        elif c == 'L': direction = (direction - steps) % 4
    min_x = min(x for x, y in visited)
    min_y = min(y for x, y in visited)
    width = max(x for x, y in visited) - min_x + 1
    height = max(y for x, y in visited) - min_y + 1
    grid = [[' '] * width for _ in range(height)]
    for x, y in visited: grid[y-min_y][x-min_x] = '*'
    return '\r\n'.join(''.join(row) for row in grid)

dx = 0, 1, 0, -1
dy = -1, 0, 1, 0

