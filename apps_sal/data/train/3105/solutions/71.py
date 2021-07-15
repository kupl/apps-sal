def count_sheep(n):
    res = ''
    count = 1
    while n > 0:
        res += "{} sheep...".format(count)
        count += 1
        n -= 1
    return res
