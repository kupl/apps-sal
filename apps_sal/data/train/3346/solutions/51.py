def is_prime(a):
    if a <= 1:
        return False
    if a <= 3:
        return True

    if a % 2 == 0 or a % 3 == 0:
        return False
    i = 5
    while i * i <= a:
        if a % i == 0 or a % (i + 2) == 0:
            return False
        i += 6
    return True


def gap(g, m, n):
    flag = 0
    start, end = -1, -1
    if m % 2 == 0:
        m += 1
    for i in range(m, n + 1, 2):
        if is_prime(i):
            if flag == 0:
                start = i
                flag = 1
            else:
                end = i
                if end - start == g:
                    return [start, end]
                else:
                    start, end = i, -1

    return None
