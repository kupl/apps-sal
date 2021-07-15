def find_mult10_SF(n):
    # ST(n) = 6 ** n + 5 ** n - 2 ** n - 1
    # SF(n) = (6 ** n + 3 * (2 ** n)) / 4
    # SF is divisible by 10 if n = 3 mod 4
    #
    # => nth 10 multiple of 10 is ST(n * 4 - 1)
    k = n * 4 - 1
    return (6 ** k + 3 * (2 ** k)) / 4
