def remove_exclamation_marks(s):
    result = ''
    for i in range(len(s)):
        if s[i] != '!':
            result += s[i]
    return result
