def interpreter(tape):
    (cells, cell, out) = ({}, 0, '')
    for c in tape:
        if c == '>':
            cell += 1
        if c == '<':
            cell -= 1
        if c == '+':
            cells[cell] = 1 if cell not in cells else 0 if cells[cell] == 255 else cells[cell] + 1
        if c == '*':
            out += chr(cells[cell])
    return out
