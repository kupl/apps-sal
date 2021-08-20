def bracket_pairs(string):
    result = {}
    stack = []
    for (i, c) in enumerate(string):
        if c == ')':
            if not stack:
                return False
            result[stack.pop()] = i
        elif c == '(':
            stack.append(i)
    if stack:
        return False
    return result
