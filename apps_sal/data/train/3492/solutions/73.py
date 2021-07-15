def correct_polish_letters(st): 
    translation = { 'ą' : 'a',
                    'ć' : 'c',
                    'ę' : 'e',
                    'ł' : 'l',
                    'ń' : 'n',
                    'ó' : 'o',
                    'ś' : 's',
                    'ź' : 'z',
                    'ż' : 'z' }
    output = ''
    for x in st:
        if x in translation:
            output += translation.get(x)
        else:
            output += x
    return output
