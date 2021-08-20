SWAPPER = str.maketrans('+-', '-+')


def solve(s):
    return simplify(iter(s)).strip('+')


def simplify(it, prevOp='+'):
    lst = []
    for c in it:
        if c == '(':
            lst.append(simplify(it, '+' if not lst else lst.pop()))
        elif c == ')':
            break
        else:
            if not lst and c.isalpha():
                lst.append('+')
            lst.append(c)
    s = ''.join(lst)
    if prevOp == '-':
        s = s.translate(SWAPPER)
    return s
