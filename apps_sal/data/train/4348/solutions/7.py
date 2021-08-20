def calc_fuel(n):
    result = {}
    n *= 11
    for (fuel, sec) in (('lava', 800), ('blaze rod', 120), ('coal', 80), ('wood', 15), ('stick', 1)):
        (result[fuel], n) = divmod(n, sec)
    return result
