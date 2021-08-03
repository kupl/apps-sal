def is_bouncy(number):
    n = str(number)

    return not(sorted(n) == list(n)) and not(sorted(n, reverse=True) == list(n))
