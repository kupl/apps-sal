operand = set("0123456789")
operator = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


def to_postfix(infix):
    stack, res = [], []
    for c in "({})".format(infix):
        if c in operand:
            res.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack[-1] != '(':
                res.append(stack.pop())
            del stack[-1]
        elif c in operator:
            while operator.get(stack[-1], 0) >= operator[c]:
                res.append(stack.pop())
            stack.append(c)
        else:
            raise Exception("Character {} unknown".format(c))
    return ''.join(res)
