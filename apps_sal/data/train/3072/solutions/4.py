def is_narcissistic(*nos):
    try:
        return all([sum([int(i) ** len(str(n)) for i in str(n)]) == int(n) for n in nos])
    except ValueError:
        return False
