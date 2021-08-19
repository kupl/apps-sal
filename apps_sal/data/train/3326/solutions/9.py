def pairs(s):
    (stack, pairs) = ([], {})
    for (i, c) in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            pairs[stack.pop()] = i
    return pairs


swap_parentheses = str.maketrans('()', ')(')


def reverse_in_parentheses(s):
    res = list(s)
    for (i, j) in pairs(s).items():
        res[i + 1:j] = ''.join(res[j - 1:i:-1]).translate(swap_parentheses)
    return ''.join(res)
