ops = {"+": (lambda x, y: x + y), "-": (lambda x, y: x - y), "*": (lambda x, y: x * y), "/": (lambda x, y: x / y)}


def calc(expr):  # obscure version
    stack, tokens = [], expr.split(" ") if expr != "" else ["0"]
    for token in tokens:
        stack.append(float(token)) if token not in ops else stack.append(ops[token](*(stack.pop(), stack.pop())[::-1]))
    return stack[-1]
