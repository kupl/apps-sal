def replace_exclamation(s):
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    ans = ''
    for i in s:
        if i in vowel:
            ans = ans + '!'
        else:
            ans = ans + i
    return ans
