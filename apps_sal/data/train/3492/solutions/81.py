def correct_polish_letters(st):
    d = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
    r = ''
    for letter in st:
        if letter in d:
            r += d[letter]
        else:
            r += letter
    return r
