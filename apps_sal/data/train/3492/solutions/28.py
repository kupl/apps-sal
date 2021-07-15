def correct_polish_letters(st): 
    dict = {
        'ą' : 'a',
        'ć' : 'c',
        'ę' : 'e',
        'ł' : 'l',
        'ń' : 'n',
        'ó' : 'o',
        'ś' : 's',
        'ź' : 'z',
        'ż' : 'z'
    }
    return ''.join(dict.get(c, c) for c in st)
