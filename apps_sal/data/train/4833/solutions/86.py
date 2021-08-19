def replace_exclamation(s):
    ans = ''
    for i in range(0, len(s)):
        if s[i] in 'aeiouAEIOU':
            ans += '!'
        else:
            ans += s[i]
    return ans
