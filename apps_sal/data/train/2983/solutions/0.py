def bouncy_count(m):
    num = den = 1
    for i in range(1, 11):
        num *= m + i + i * (i == 10)
        den *= i
    return 10 ** m - num // den + 10 * m + 1
