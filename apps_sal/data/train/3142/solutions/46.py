def seven_ate9(s):
    s2 = s[0]
    for i, v in enumerate(s[1:], 1):
        try:
            if s[i - 1] == s[i + 1] == "7" and v == "9":
                continue
            else:
                s2 += v
        except:
            break

    return s2 + s[-1]
