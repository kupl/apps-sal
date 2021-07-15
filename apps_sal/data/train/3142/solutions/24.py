def seven_ate9(s):
    return s[0] + "".join(
        [s[i] for i in range(1, len(s) - 1) if not (s[i - 1] == '7' and s[i] == '9' and s[i + 1] == '7')]) + s[-1]
