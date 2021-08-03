def last_digit(n1, n2):
    return (n1 % 10) ** (n2 % 4 + 4 * bool(n2)) % 10
