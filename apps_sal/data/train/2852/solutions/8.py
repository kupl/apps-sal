def find_longest(st):
    positions = []
    stack = []
    for (i, ch) in enumerate(st):
        if ch == '(':
            stack.append(i)
        elif stack:
            positions.append(stack.pop())
            positions.append(i)
    prev = float('-inf')
    cons = 0
    ans = 0
    for (i, p) in enumerate(sorted(positions)):
        if p == prev + 1:
            cons += 1
        else:
            ans = max(ans, cons)
            cons = 1
        prev = p
    return max(ans, cons)
