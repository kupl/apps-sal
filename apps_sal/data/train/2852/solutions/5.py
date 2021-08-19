def find_longest(st):
    (stack, max_so_far) = ([-1], 0)
    for ind in range(len(st)):
        if st[ind] == '(':
            stack.append(ind)
        else:
            stack.pop()
            if len(stack) > 0:
                max_so_far = max(max_so_far, ind - stack[-1])
            else:
                stack.append(ind)
    return max_so_far
