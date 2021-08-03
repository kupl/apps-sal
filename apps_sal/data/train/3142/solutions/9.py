def seven_ate9(s):
    return ''.join(s[i] for i in range(len(s)) if s[i - 1:i + 2] != '797')
