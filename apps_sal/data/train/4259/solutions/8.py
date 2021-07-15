def pattern(n, *args):
    if n < 1:
        return ''
    x = 1 if len(args) == 0 else max(args[0], 1)
    width, height = (1 + 2*(n-1)*x), 2*n - 1
    pict = [[' '] * width for _ in range(height)]
    x_positions = set()
    for x in range(0, width, 2*(n-1)):
        x_positions.add(('r', x))
        x_positions.add(('l', x))
    for y, n in enumerate(list(range(1, n+1)) + list(range(n-1, 0, -1))):
        new_x_positions = set()
        for d, x in x_positions:
            pict[y][x] = str(n)[-1]
            if d == 'r' and x + 1 < width:
                new_x_positions.add((d, x+1))
            elif d == 'l' and 0 <= x - 1:
                new_x_positions.add((d, x-1))
        x_positions = new_x_positions
    return '\n'.join(map(''.join, pict))
