def isInvalid(lines, y, x, chars):
    if y >= len(lines) or x >= len(lines[y]):
        return True
    return lines[y][x] not in chars


def isSquare(lines, x, y, size):
    if isInvalid(lines, y, x, '+') or \
       isInvalid(lines, y + size, x, '+') or \
       isInvalid(lines, y, x + size, '+') or \
       isInvalid(lines, y + size, x + size, '+'):
        return False
    for s in range(size + 1):
        if isInvalid(lines, y, x + s, '+-') or \
           isInvalid(lines, y + s, x, '+|') or \
           isInvalid(lines, y + size, x + s, '+-') or \
           isInvalid(lines, y + s, x + size, '+|'):
            return False
    return True


def count_squares(lines):
    count = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            for s in range(1, min(len(lines) - y, len(lines[y]) - x)):
                if isSquare(lines, x, y, s):
                    count += 1
    return count
