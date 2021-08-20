def solve(s, idx):
    stack = []
    for (i, c) in enumerate(s):
        if c == '(':
            stack += [i]
        if c == ')':
            if not stack:
                break
            if stack.pop() == idx:
                return i
    return -1
