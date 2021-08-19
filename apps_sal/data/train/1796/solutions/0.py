def to_postfix(infix):
    prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0}
    postfix = []
    stack = []
    for ch in infix:
        if ch in '0123456789':
            postfix.append(ch)
        elif ch in '(':
            stack.append(ch)
        elif ch in ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and prec[stack[-1]] >= prec[ch]:
                postfix.append(stack.pop())
            stack.append(ch)
    while stack:
        postfix.append(stack.pop())
    return ''.join(postfix)
