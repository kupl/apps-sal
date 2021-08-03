def simplify(n):
    div, sq, root = 2, 1, 1
    while div <= n:
        r = 0
        while n % div == 0:
            n //= div
            r += 1
        sq *= div ** (r // 2)
        root *= div ** (r % 2)
        div += 1 + (div != 2)
    return (
        f'{sq}' if root == 1 else
        f'sqrt {root}' if sq == 1 else
        f'{sq} sqrt {root}'
    )


def desimplify(s):
    xs = ([int(x.strip() or 0) for x in s.split('sqrt')] + [0])[:2]
    return (xs[0] ** 2 * xs[1]) or (xs[0] ** 2 + xs[1])
