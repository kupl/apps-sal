def number(lines):
    i = 1
    res = []
    for line in lines:
        res.append(f"{i}: {line}")
        i += 1
    return res
