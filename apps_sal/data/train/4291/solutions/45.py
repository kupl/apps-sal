def century(year):
    (a, b) = divmod(year, 100)
    return a + 2 * b // (b + 1)
