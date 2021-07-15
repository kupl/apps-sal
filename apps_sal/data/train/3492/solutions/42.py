def correct_polish_letters(st): 
    polish_alphabet = {
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
    return ''.join([polish_alphabet.get(i) if i in polish_alphabet else i for i in st])
