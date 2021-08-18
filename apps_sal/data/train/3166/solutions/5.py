def circle_slash(n):
    if (n & (n - 1)) == 0:
        return 1
    result = 1
    while result < n:
        result = result << 1
    return (n - result / 2) * 2 + 1
