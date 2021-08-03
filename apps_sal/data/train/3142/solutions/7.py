def seven_ate9(s):
    return ''.join('' if x == '9' and s[y - 1:y + 2] == '797' else x for y, x in enumerate(s))
