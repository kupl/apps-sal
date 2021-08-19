def double_char(s):
    return ''.join((''.join(i) for i in zip(s, s)))
