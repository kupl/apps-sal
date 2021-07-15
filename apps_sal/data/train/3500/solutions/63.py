def remove_exclamation_marks(s):
    res = ''
    for i in range(len(s)):
        if s[i] != '!':
            res += s[i]
    return res
