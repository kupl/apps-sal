def correct_polish_letters(st):
    dic = {
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
    res = "".join(dic[i] if i in dic else i for i in st)
    return res
