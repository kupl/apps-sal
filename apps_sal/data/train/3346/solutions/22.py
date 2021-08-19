def prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def gap(g, m, n):
    res = []
    i = m
    while i < n + 1:
        if prime(i):
            res.append(i)
            break
        i += 1
    while True:
        j = i + 1
        while j < n + 1:
            if prime(j):
                if j - i == g:
                    res.append(j)
                    return res
                else:
                    res[0] = j
                    i = j
            j += 1
        return None
