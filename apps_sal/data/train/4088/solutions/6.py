def tetris(lst):
    (field, lines) = ([0] * 9, 0)
    for (h, s, m) in lst:
        i = 4 + int(m) * (-1 if s == 'L' else 1)
        field[i] += int(h)
        while all((col > 0 for col in field)):
            (field, lines) = ([col - 1 for col in field], lines + 1)
        if field[i] > 29:
            break
    return lines
