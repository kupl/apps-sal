def two_decimal_places(n):
    #    raise NotImplementedError("TODO: two_decimal_places")
    if (1000 * n % 10 == 5):
        return round((1000 * n + 1) / 1000, 2)
    return round(n, 2)
