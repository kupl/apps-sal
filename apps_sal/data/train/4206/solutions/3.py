def three_details(n):
    u = 2 ** n.bit_length()
    return n - u // 2 if n <= 3 * u // 4 else u - n
