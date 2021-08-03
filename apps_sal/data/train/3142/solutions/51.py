def seven_ate9(s):
    result = ""
    for i, c in enumerate(s):
        if s[i - 1:i + 2] != "797":
            result += c
    return result
