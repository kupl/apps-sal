def valid_parentheses(string):
    depth = 0
    for i in string:
        if i == '(':
            depth += 1
        elif i == ')':
            depth -= 1
        if depth < 0:
            return False
    if depth == 0:
        return True
    else:
        return False
