def x(n):
    return '\n'.join(''.join('■' if row == col or row == n - 1 - col else '□' for col in range(n)) for row in range(n))
