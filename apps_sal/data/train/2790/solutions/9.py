def dup(arry):
    stack = []
    output = []
    for item in arry:
        for i in item:
            if len(stack) == 0 or (len(stack) >= 1 and i != stack[-1]):
                stack.append(i)
            else:
                continue
        output.append(''.join(stack))
        stack = []
    return output
