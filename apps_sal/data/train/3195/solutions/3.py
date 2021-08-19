def braces_status(string):
    stack = []
    corresp = {')': '(', '}': '{', ']': '['}
    for c in (s for s in string if s in '()[]{}'):
        if c in '([{':
            stack.append(c)
        elif not stack or stack.pop() != corresp[c]:
            return False
    return not stack
