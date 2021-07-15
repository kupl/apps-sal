def checkered_board(size):
    result = ''
    rows = []
    print(size, type(size))
    if not type(size) == int:
        return False
    if size < 2:
        return False
    if size % 2 == 0:
        a = '□'
        b = '■'
    else:
        a = '■'
        b = '□'
    for x in range(size):
        if x % 2 == 0:
            row = [a if x % 2 == 0 else b for x in range(size)]
        else:
            row = [b if x % 2 == 0 else a for x in range(size)]
        rows.append(' '.join(row))
        result = '\n'.join(rows)
    return result
