def number(lines):
    res = []
    for i in range(1, len(lines) + 1):
        res.append(f'{i}: {lines[i-1]}')
    return res
