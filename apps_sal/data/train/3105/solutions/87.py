def count_sheep(n):
    ans = ''
    for i in range(n):
        ans = ans + '{} sheep...'.format(i + 1)
    return ans
