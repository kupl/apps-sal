def replace_exclamation(s):
    ans = ''
    vowels = 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'
    for char in s:
        if char in vowels:
            ans += '!'
        else:
            ans += char
    return ans
