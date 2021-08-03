def diagonal(line, diag):
    s, j, p = 1, 1, 1
    for i in range(diag + 1, line + 1):
        p = p * i // j
        s += p
        j += 1
    return s
