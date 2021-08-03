def get_sum(x):
    return sum(int(t) for t in list(str(x)))


def is_very_even_number(n):
    result = get_sum(n)
    while len(str(result)) >= 2:
        result = get_sum(result)
    return (result % 2 == 0)
