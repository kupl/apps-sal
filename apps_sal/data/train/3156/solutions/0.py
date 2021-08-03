def is_even(x):
    return all(int(i) % 2 == 0 for i in str(x))


def even_digit_squares(a, b):
    first = int(a ** (1 / 2)) + 1
    last = int(b ** (1 / 2)) + 1
    return sorted([x * x for x in range(first, last) if is_even(x * x)])
