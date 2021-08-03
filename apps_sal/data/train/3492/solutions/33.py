def correct_polish_letters(st):
    d = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
         'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
    ans = ''
    for char in st:
        if char in d:
            ans += d[char]
        else:
            ans += char
    return ans
