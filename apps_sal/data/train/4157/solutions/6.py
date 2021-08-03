parens = dict([')(', '][', '}{'])


def group_check(s):
    stack = []
    for c in s:
        if c in parens:
            if not (stack and parens[c] == stack.pop()):
                return False
        else:
            stack.append(c)
    return not stack
