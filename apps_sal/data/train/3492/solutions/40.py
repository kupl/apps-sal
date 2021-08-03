def correct_polish_letters(st):
    dict = {
        'ą': 'a',
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
    str = ''
    for letter in st:
        if letter in dict:
            str += dict[letter]
        else:
            str += letter
    return str
