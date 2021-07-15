def is_triangle(a, b, c):
    table = [a, b, c]
    table.sort()
    return table[0] + table[1] > table[2]

