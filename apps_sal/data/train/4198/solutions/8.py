import re

def simplify(n: int) -> str:
    def inner(n):
        for i in range(2, n):
            div, mod = divmod(n, i * i)
            if not mod:
                sq1, sq2 = inner(div)
                return (i * sq1, sq2)
            if not div:
                break
        return (1, n)
    a, b = inner(n)
    if b == 1:
        return f'{a}'
    elif a != 1:
        return f'{a} sqrt {b}'
    else:
        return f'sqrt {b}'

def desimplify(s: str) -> int:
    m = re.match(r'(?P<INT>\d+)?(?: )?(?:sqrt (?P<SQRT>\d+))?', s)
    x, y = m.groups()
    return int(x or '1') ** 2 * int(y or '1')
