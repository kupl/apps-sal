def correct_polish_letters(st):
    diacritic = {'ą': 'a',
                 'ć': 'c',
                 'ę': 'e',
                 'ł': 'l',
                 'ń': 'n',
                 'ó': 'o',
                 'ś': 's',
                 'ź': 'z',
                 'ż': 'z'}
    return ''.join([char.replace(char, diacritic[char]) if char in diacritic.keys() else char for char in st])
