def find_difference(a, b):
    total_a = 1
    total_b = 1
    for i in a:
        total_a *= i
    for c in b:
        total_b *= c
    return abs(total_a - total_b)
