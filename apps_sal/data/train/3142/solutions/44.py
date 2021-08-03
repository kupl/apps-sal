def seven_ate9(s):
    return ''.join(['' if s[i - 1:i + 2] == '797' else s[i] for i in range(len(s))])
