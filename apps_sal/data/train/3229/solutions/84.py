def am_i_wilson(n):
    a = 1
    if n == 0 or n == 1 or n > 1000:
        return False

    for i in range(1, n):
        a *= i

    return True if (a + 1) % (n * n) == 0 else False
