def reverse(s):
    ss = ''
    for i in range(len(s)):
        if i > 0 and s[i] == s[i - 1] or (i < len(s) - 1 and s[i] == s[i + 1]):
            ss += s[i].swapcase()
        else:
            ss += s[i]
    return ss
