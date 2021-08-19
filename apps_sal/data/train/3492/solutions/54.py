def correct_polish_letters(st):
    diacritics = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
    return ''.join([diacritics.get(c) if diacritics.get(c) else c for c in st])
