def interpreter(code, iterations, width, height):
    grid = [[0 for r in range(width)] for c in range(height)]
    t = iterations
    w, h = width, height
    stack, bracket_pos = [], {}
    for i, c in enumerate(code):
        if c == "[": 
            stack.append(i)
        elif c == "]": 
            bracket_pos[i] = stack[-1]
            bracket_pos[stack.pop()] = i

    a, b, p = 0, 0, 0    
    while t > 0 and p < len(code):
        if code[p] == "e": b += 1
        elif code[p] == "w": b -= 1
        elif code[p] == "s": a += 1
        elif code[p] == "n": a -= 1
        elif code[p] == "*": grid[a%h][b%w] ^= 1
        
        elif code[p] == "[":
            if grid[a%h][b%w] == 0:
                p = bracket_pos[p]
        elif code[p] == "]":
            if grid[a%h][b%w] == 1: 
                p = bracket_pos[p]
        else: t += 1
        t -= 1
        p += 1
    return "\r\n".join("".join(map(str, g)) for g in grid)
