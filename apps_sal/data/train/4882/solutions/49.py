def round_to_next5(n):
    if n % 5:
        if n > 0:
            return (5 * int(n / 5)) + 5
        else:
            return (5 * int(n / 5))
    else:
        return 5 * int(n / 5)
