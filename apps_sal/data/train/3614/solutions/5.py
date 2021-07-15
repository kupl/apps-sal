def interpreter(tape):
    selector = 0
    cells = dict()
    output = ''
    for c in tape:
        if c == '>':
            selector += 1
        elif c == '<':
            selector -= 1
        elif c == '*':
            output += chr(cells.get(selector, 0))
        elif c == '+':
            cells[selector] = (cells.get(selector, 0) + 1) % 256
        elif c == '-':
            cells[selector] = (cells.get(selector, 0) - 1) % 256
        elif c == '/':
            cells[selector] = 0
        elif c == '!':
            cells[len(cells)] = 0
    return output
