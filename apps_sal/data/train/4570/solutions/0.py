def clean_string(s):
    stk = []
    for c in s:
        if c == '
        stk.pop()
        elif c != '
        stk.append(c)
    return ''.join(stk)
