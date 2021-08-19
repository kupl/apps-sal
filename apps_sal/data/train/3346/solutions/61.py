def gap(g, m, n):
    # your code
    for i in range(m, n + 1):
        if is_prime(i):
            if is_prime(i + g):
                for j in range(i + 1, i + g):
                    if is_prime(j):
                        break
                else:
                    return [i, i + g]
            else:
                continue
        else:
            continue
    return None


def is_prime(num):
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
