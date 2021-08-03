def folding(a, b):
    count = 0
    while a != b:
        if a < b:
            a, b = b, a
        a = a - b
        count += 1
    return count + 1
