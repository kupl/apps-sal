import re


def no_order(equation):
    ops = {'+': lambda l, r: l + r, '-': lambda l, r: l - r, '*': lambda l, r: l * r, '/': lambda l, r: l // r if r != 0 else None, '^': lambda l, r: l ** r, '%': lambda l, r: l % r if r != 0 else None}
    expr = re.sub('[\\s\\t]+', '', equation.strip())
    expr = re.sub('(?<=\\W)(?=[\\d\\s])|(?<=[\\d\\s])(?=\\W)', '\x0c', expr).split('\x0c')
    temp = expr[0]
    for i in range(1, len(expr), 2):
        temp = ops[expr[i]](int(temp), int(expr[i + 1]))
        if temp is None:
            break
    if temp is not None:
        return int(temp)
    return temp
