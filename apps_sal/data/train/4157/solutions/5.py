OPENING = '([{'
CLOSING = dict(['()', '[]', '{}'])


def group_check(s):
    stack = []
    for c in s:
        if c in OPENING:
            stack.append(CLOSING[c])
        else:
            if len(stack) == 0 or c != stack.pop():
                return False
    return len(stack) == 0
