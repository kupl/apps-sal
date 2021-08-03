def folding(a, b):
    count = 0
    while a > 0 and b > 0:
        a, b, count = max(a - b, b), min(a - b, b), count + 1
    return count
