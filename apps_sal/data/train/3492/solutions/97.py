def correct_polish_letters(st):
    polish_letters = {'ą': 'a',
                      'ć': 'c',
                      'ę': 'e',
                      'ł': 'l',
                      'ń': 'n',
                      'ó': 'o',
                      'ś': 's',
                      'ź': 'z',
                      'ż': 'z'}
    ret = ''
    for i in st:
        if i in polish_letters.keys():
            ret += polish_letters[i]
        else:
            ret += i
    return ret
