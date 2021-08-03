def calc(expr):
    stack = []
    [stack.append(eval("{1}{2}{0}".format(stack.pop(), stack.pop(), e)) if e in ('+', '-', '/', '*') else e) for e in expr.split()]
    return float(stack.pop()) if stack else 0
