def interpreter(tape):
    cells = [ 0 for _ in range(100)]
    output = ''
    ptr = 0
    for i in tape:
        if i == '>':
            ptr += 1
        elif i == '<':
            ptr -= 1
        elif i == '+':
            cells[ptr] += 1
            cells[ptr] %= 256
        elif i == '*':
            output += chr(cells[ptr])
        else:
            pass
    return output

