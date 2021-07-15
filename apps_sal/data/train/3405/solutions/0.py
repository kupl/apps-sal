def is_pandigital(n):
    s = str(n)
    return not '0' in s and len(set(s)) == len(s)

def pow_root_pandigit(val, n, k):
    res = []
    current = int(round(val ** (1.0 / n), 5)) + 1
    while len(res) < k and current <= 987654321 ** (1.0 / n):
        if is_pandigital(current):
            p = current ** n
            if is_pandigital(p):
                res += [[current, p]]
        current += 1
    return res if len(res) != 1 else res[0]
