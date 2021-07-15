def find_longest(s):
    stack, m = [-1], 0
    for i,j in enumerate(s):
        if j == '(' : stack.append(i)
        else:
            stack.pop()
            if stack : m = max(m,i-stack[-1])
            else : stack.append(i)
    return m
