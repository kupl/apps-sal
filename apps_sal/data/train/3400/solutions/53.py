def even_numbers(a, n):
    return [x for x in a[::-1] if x % 2 == 0][:n][::-1]
