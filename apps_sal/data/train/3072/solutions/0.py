def get_digits(n):
    return [int(x) for x in list(str(n))]


def is_narc(n):
    return n == sum([x ** len(get_digits(n)) for x in get_digits(n)])


def is_narcissistic(*values):
    try:
        return all((type(n) in [int, str] and is_narc(int(n)) for n in values))
    except ValueError:
        return False
