def valid_parentheses(string):
    stack = []
    for i in string:
        if i == '(':
            stack.append(i)
        elif i == ')' and (not stack):
            return False
        elif i == ')':
            stack.pop()
    return not stack
