from functools import reduce


def calculate_next_el(prev_el):
    if prev_el < 10:
        return 2 * prev_el
    else:
        multiplication = reduce((lambda x, y: x * y), [x for x in map(int, str(prev_el)) if x > 0], 1)
        return prev_el + multiplication


def generate_series(start):
    last = start
    while True:
        last = calculate_next_el(last)
        yield last


def convergence(n):
    current_base = 1
    current_test = n
    base_series = generate_series(current_base)
    test_series = generate_series(current_test)
    result = 0
    while current_base != current_test:
        if current_base < current_test:
            current_base = base_series.__next__()
        else:
            current_test = test_series.__next__()
            result += 1
    return result
