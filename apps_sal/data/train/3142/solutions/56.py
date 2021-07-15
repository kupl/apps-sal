def seven_ate9(s):
    res = ''
    i = 0
    while i < len(s):
        res += s[i]
        i += 1 + ((i + 2) < len(s) and s[i:i+3] == "797")
    return res
