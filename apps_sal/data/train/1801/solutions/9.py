def interpreter(code, iterations, width, height):
    matrix = [[0 for i in range(width)] for i in range(height)]
    i = 0
    iteration = 0
    p = [0, 0]
    s = []
    mate = {}
    for k in range(len(code)):
        c = code[k]
        if c == '[':
            s.append(k)
        if c == ']':
            m = s.pop()
            mate[m] = k
            mate[k] = m
    while iteration < iterations and i < len(code):
        c = code[i]
        if c == '*':
            matrix[p[1]][p[0]] ^= 1
        elif c == 'n':
            p[1] = (p[1] - 1) % height
        elif c == 'e':
            p[0] = (p[0] + 1) % width
        elif c == 's':
            p[1] = (p[1] + 1) % height
        elif c == 'w':
            p[0] = (p[0] - 1) % width
        elif c == '[':
            if not matrix[p[1]][p[0]]:
                i = mate[i]
        elif c == ']':
            if matrix[p[1]][p[0]]:
                i = mate[i]
        else:
            iteration -= 1
        i += 1
        iteration += 1
    return '\r\n'.join([''.join([str(matrix[y][x]) for x in range(width)]) for y in range(height)])
