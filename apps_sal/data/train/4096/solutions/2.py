iparens = iter('(){}[]<>')
parens = dict(zip(iparens, iparens))
closing = parens.values()


def valid_parentheses(astr):
    stack = []
    for c in astr:
        d = parens.get(c, None)
        if d:
            stack.append(d)
        elif c in closing:
            if not stack or c != stack.pop():
                return False
    return not stack
