def remove_parentheses(s):
    para = ('(', ')')
    stack = []
    string = []
    for char in s:
        if char in para:
            stack.append(char) if char == para[0] else stack.pop()
        elif len(stack) == 0:
            string.append(char)
    return ''.join(string)
