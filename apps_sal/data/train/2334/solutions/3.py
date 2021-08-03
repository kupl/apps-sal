for t in range(int(input())):
    s = input()
    stack = []
    for i in s:
        if i == 'A':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                stack.append(i)
    print(len(stack))
