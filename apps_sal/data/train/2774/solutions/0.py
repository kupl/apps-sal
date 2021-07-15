def is_balanced(s, caps):
    stack = []
    openers, closers = caps[::2], caps[1::2]
    for char in s:
        if char in openers:
            if char in closers and stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        elif char in closers:
            if not stack or openers[closers.index(char)] != stack[-1]:
                return False
            else:
                stack.pop()
    return not stack
