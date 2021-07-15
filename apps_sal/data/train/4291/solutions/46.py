def century(year):
    a, b = divmod(year, 100)
    return (a + 1) - (not b)
