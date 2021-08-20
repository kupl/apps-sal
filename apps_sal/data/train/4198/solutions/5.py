def simplify(n):
    if n ** 0.5 % 1 == 0:
        return f'{int(n ** 0.5)}'
    d = 1
    r = n
    for i in range(n // 2, 1, -1):
        if n % i == 0 and i ** 0.5 % 1 == 0:
            r = n // i
            d = int(i ** 0.5)
            break
    return f'{d} sqrt {r}' if d > 1 else f'sqrt {r}'


def desimplify(s):
    if s.find('sqrt') == -1:
        return int(s) ** 2
    elif s.count(' ') == 1:
        return int(s[s.index(' ') + 1:])
    else:
        n1 = int(s[:s.index(' ')])
        n2 = int(s[s.rindex(' ') + 1:])
        return n1 ** 2 * n2
