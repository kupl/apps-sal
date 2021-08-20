def remove_parentheses(s):

    def f():
        paren = 0
        for c in s:
            if c == '(':
                paren += 1
            elif c == ')':
                paren -= 1
            elif not paren:
                yield c
    return ''.join(f())
