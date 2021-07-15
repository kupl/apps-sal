def replace_exclamation(s):
    vowel = 'aeiouAEIOU'
    res = ''
    for c in s:
        if c in vowel:
            res += '!'
        else:
            res += c
    return res
