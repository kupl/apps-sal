def correct_polish_letters(st): 
    rules = {
        'ą': 'a',
        'ć': 'c',
        'ę': 'e',
        'ł': 'l',
        'ń': 'n',
        'ó': 'o',
        'ś': 's',
        'ź': 'z',
        'ż': 'z'
        }
    return ''.join(map(lambda c: rules[c] if c in rules else c, st))
