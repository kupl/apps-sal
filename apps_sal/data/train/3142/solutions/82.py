def seven_ate9(s):
    res = s[0]
    for (i, c) in enumerate(s[1:-1]):
        if c == '9' and s[i] == '7' and (s[i + 2] == '7'):
            pass
        else:
            res += c
    res += s[-1]
    return res
