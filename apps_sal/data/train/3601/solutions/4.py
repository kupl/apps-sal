def find_nb(m):
    total, i = 1, 2
    while total < m:
        total += i * i * i
        i += 1
    return i - 1 if total == m else -1
