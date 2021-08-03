def find_difference(a, b):
    value_a = a[0] * a[1] * a[2]
    value_b = b[0] * b[1] * b[2]
    return value_a - value_b if value_a >= value_b else value_b - value_a
