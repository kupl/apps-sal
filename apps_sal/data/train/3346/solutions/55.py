from math import sqrt


def gap(g, m, n):
    pass_prime = 2
    for i in range(m, n + 1):
        list = [2] + [i for i in range(3, int(sqrt(i) + 1.5), 2)]
        ind = 0
        for j in list:
            if i % j == 0:
                ind = 1
                break
        if ind == 0:
            if i - pass_prime == g:
                return [pass_prime, i]
            pass_prime = i
    return None
