def find_difference(a, b):
    total_a = 1
    for i in range(0, len(a)):
        total_a *= a[i]
    total_b = 1
    for j in range(0, len(b)):
        total_b *= b[j]
    return abs(total_a - total_b)
