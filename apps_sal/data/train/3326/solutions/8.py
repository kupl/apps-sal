swap_parentheses = str.maketrans('()', ')(')


def reverse_in_parentheses(s):
    stack, res = [], list(s)
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            j = stack.pop()
            res[j + 1:i] = ''.join(res[i - 1:j:-1]).translate(swap_parentheses)
    return ''.join(res)
