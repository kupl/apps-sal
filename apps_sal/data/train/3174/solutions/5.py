import re


def derivative(eq):
    res = []

    eq = re.sub(r'\bx', '1x', eq)

    for const, var, exp in re.findall(r'([+-]?\d+)(x?)\^?(\d*)', eq):

        if not var:
            continue

        if not exp:
            res.append(const)
            continue

        const, exp = int(const), int(exp)
        const *= exp
        if exp == 2:
            res.append('%+dx' % const)
        else:
            res.append('%+dx^%d' % (const, exp - 1))

    res = ''.join(res).strip('+')
    return res if res else '0'
