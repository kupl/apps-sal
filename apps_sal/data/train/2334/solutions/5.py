t = int(input())
for i in range(t):
    s = input()
    stack = []
    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        elif s[i] == 'B' and (stack[-1] == 'A' or stack[-1] == 'B'):
            stack.pop()
        else:
            stack.append(s[i])
    print(len(stack))
