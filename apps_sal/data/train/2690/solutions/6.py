def remove_parentheses(s):
    stack = []
    for i in range(len(s)):
        if s[i] is not ')':
            stack.append(s[i])
        else:
            while(stack[-1]!='('):
                stack.pop()
            stack.pop()
    return ''.join(stack)
