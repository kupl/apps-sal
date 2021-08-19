def seven_ate9(s):
    return s[0] + ''.join((s[i + 1] for i in range(len(s) - 2) if s[i + 1] != '9' or s[i] + s[i + 2] != '77')) + s[-1]
