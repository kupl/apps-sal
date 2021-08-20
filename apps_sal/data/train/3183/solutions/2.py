import itertools


def interpreter(tape):
    (cells, cell, out, skip) = ({}, 0, '', False)
    for c in itertools.cycle(tape):
        if not skip:
            if c == '>':
                cell += 1
            if c == '<':
                cell -= 1
            if c == '+':
                cells[cell] = 1 if cell not in cells else 0 if cells[cell] == 255 else cells[cell] + 1
            if c == '-':
                cells[cell] = 255 if cell not in cells else 255 if cells[cell] == 0 else cells[cell] - 1
            if c == '*':
                out += chr(cells.get(cell, 0))
            if c == '&':
                break
        skip = c == '/' and cells.get(cell, 0) == 0 or (c == '\\' and cells.get(cell, 0))
    return out
