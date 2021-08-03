operator = set(['+', '-', '*', '/'])


def calc(expr):
    stack = list()
    for c in expr.split():
        if c in operator:
            first = stack.pop()
            second = stack.pop()
            stack.append(str(eval(second + c + first)))
        else:
            stack.append(c)
    return eval(stack.pop()) if stack else 0
