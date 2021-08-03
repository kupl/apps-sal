def interpreter(code, iterations, width, height):
    grid = [[0] * width for _ in range(height)]
    code = [c for c in code if c in '[]nesw*']

    jumps, stack = {}, []
    for i, c in enumerate(code):
        if c == '[':
            stack.append(i)
        if c == ']':
            jumps[i] = stack.pop()
            jumps[jumps[i]] = i

    ptr, x, y = -1, 0, 0
    while iterations > 0 and ptr < len(code) - 1:
        ptr += 1
        iterations -= 1
        c = code[ptr]
        if c == 'n':
            y = (y - 1) % height
        if c == 's':
            y = (y + 1) % height
        if c == 'w':
            x = (x - 1) % width
        if c == 'e':
            x = (x + 1) % width
        if c == '*':
            grid[y][x] = 1 - grid[y][x]
        if c == '[' and not grid[y][x]:
            ptr = jumps[ptr]
        if c == ']' and grid[y][x]:
            ptr = jumps[ptr]

    return '\r\n'.join(''.join(map(str, row)) for row in grid)
