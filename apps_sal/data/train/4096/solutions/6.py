def valid_parentheses(s):
    stack = 0
    for char in s:
        if char == '(':
            stack += 1
        if char == ')':
            if not stack:
                return False
            else:
                stack -= 1
    return not stack
