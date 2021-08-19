def check_vowel(s, t):
    if t == 0 and s[t] in 'aioueAEIOU':
        return True
    return True if t > 0 and t < len(s) and (s[t] in 'aioueAEIOU') else False
    pass
