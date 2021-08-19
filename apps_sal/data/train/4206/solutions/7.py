def three_details(n):
    p = 2 ** n.bit_length()
    return (p - abs(4 * n - 3 * p)) // 4
