def count_divisors(n):
    rt = int(n ** .5)
    su = 0

    for k in range(1, rt + 1):
        su += n // k

    return 2 * su - rt * rt
