def braces_status(s):
    matching = {"}":"{","]":"[",")":"("}
    stack = []
    for c in s:
        if c in "[({":
            stack.append(c)
        elif c in matching and (not stack or stack.pop() != matching[c]):
            return False
    return not stack
