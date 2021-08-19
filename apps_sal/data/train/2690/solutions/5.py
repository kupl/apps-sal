def remove_parentheses(s):
    nested = 0
    result = []
    for c in s:
        if c == '(':
            nested += 1
        elif c == ')':
            nested -= 1
        elif nested == 0:
            result.append(c)
    return ''.join(result)
