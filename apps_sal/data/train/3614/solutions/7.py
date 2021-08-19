def interpreter(tape):
    (cell, cells, out) = (0, [0], '')
    for c in [k for k in tape if k in '<>!*+-/']:
        if c == '>':
            cell += 1
        if c == '<':
            cell -= 1
        if c == '!':
            cells += [0]
        if c == '*':
            out += chr(cells[cell] if cell >= 0 and cell < len(cells) else 0)
        if cell >= 0 and cell < len(cells):
            if c == '+':
                cells[cell] += 1
            if c == '-':
                cells[cell] -= 1
            if c == '/':
                cells[cell] = 0
            cells[cell] = {256: 0, -1: 255}.get(cells[cell], cells[cell])
    return out
