def double_check(strng):
    s = strng.upper()
    return any([s[i] == s[i+1] for i in range(len(strng) - 1)])
