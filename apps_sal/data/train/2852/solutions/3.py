def find_longest(st):
    stack = [-1]
    longest = 0
    for index in range(0, len(st)):
        if st[index] == '(':
            stack.append(index)
        else:
            stack.pop()
            if stack:
                longest = max(longest, index - stack[-1])
            else:
                stack.append(index)
    print(longest)
    return longest
