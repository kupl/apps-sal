def highest_value(a, b):
    ascii_values_a = [ord(c) for c in a]
    ascii_values_b = [ord(c) for c in b]
    if sum(ascii_values_a) > sum(ascii_values_b) or sum(ascii_values_a) == sum(ascii_values_b):
        return a
    return b
