for i in range(int(input())):
    s = input()
    stack = []
    ans = 0
    c = 0
    for i in range(len(s)):
        if s[i] == "<":
            stack.append(s[i])
            c += 1
        else:
            if (len(stack) == 0) or (stack[-1] != "<"):
                break
            else:
                stack.pop()
                if len(stack) == 0:
                    ans += (2 * c)
                    c = 0
    print(ans)
