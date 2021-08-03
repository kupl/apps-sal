def is_pandigital(n):
    s = set(c for c in str(n) if c != "0")
    if len(s) != len(str(n)):
        return False
    else:
        return True


def pow_root_pandigit(val, n, k):

    i, l = int(val**(1.0 / n)) - 1, []
    while len(l) < k:
        if i**n > val and is_pandigital(i) and is_pandigital(i**n):
            l.append([i, i**n])
        i += 1

        # largest possible
        if i**n > 987654321:
            break

    if len(l) == 1:
        return l[0]
    else:
        return l
