def interpreter(code, iterations, width, height):
    code = "".join(c for c in code if c in "[news]*")
    canvas = [ [0] * width for _ in range(height) ]
    row = col = step = count = loop = 0
    
    while step < len(code) and count < iterations:
        command = code[step]
        
        if loop:
            if   command == "[": loop += 1
            elif command == "]": loop -= 1
        
        elif command == "n": row = (row - 1) % height
        elif command == "s": row = (row + 1) % height
        elif command == "w": col = (col - 1) % width
        elif command == "e": col = (col + 1) % width
        elif command == "*": canvas[row][col] ^= 1
        elif command == "[" and canvas[row][col] == 0: loop += 1
        elif command == "]" and canvas[row][col] != 0: loop -= 1
        
        step += 1 if not loop else loop // abs(loop)
        count += 1 if not loop else 0
    
    return "\r\n".join("".join(map(str, row)) for row in canvas)
