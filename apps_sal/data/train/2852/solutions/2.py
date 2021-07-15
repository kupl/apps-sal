def find_longest(st):
    longest_run, stack = 0, [-1]
    for i, c in enumerate(st):
        if c == ")":
            stack.pop()
            if stack:
                longest_run = max(longest_run, i-stack[-1])
                continue
        stack.append(i)
    return longest_run
