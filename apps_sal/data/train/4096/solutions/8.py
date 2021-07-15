def valid_parentheses(s):
    b = 0
    for c in s:
        if c == '(': b += 1
        if c == ')':
            b -= 1
            if b < 0: return False
    return b == 0
