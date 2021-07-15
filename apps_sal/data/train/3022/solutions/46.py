def two_highest(arg1):
    s = sorted(set(arg1), reverse=1)
    return [s[0],s[1]] if len(s) > 1 else s
