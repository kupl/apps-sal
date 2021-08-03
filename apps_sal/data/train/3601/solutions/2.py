def find_nb(m):
    i, sum = 1, 1
    while sum < m:
        i += 1
        sum += i**3
    return i if m == sum else -1
