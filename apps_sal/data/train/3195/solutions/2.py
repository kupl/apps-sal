parens = dict([')(', '][', '}{'])
opens = set(parens.values())


def braces_status(s):
    stack = []
    for c in s:
        if c in opens:
            stack.append(c)
        elif c in parens:
            if not (stack and stack.pop() == parens[c]):
                return False
    return not stack
