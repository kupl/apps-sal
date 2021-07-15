def seven_ate9(s):
    return "".join(s[i] for i in range(0, len(s)) if s[i-1:i+2] != '797')
