def braces_status(s):
    paren = {')': '(', ']': '[', '}': '{'}
    opened = []
    for c in s:
        if c in paren.values():
            opened.append(ord(c))
        elif c in paren:
            if not opened or opened.pop() != ord(paren[c]):
                return False
    return not opened
