def correct_polish_letters(st): 
    polish = {
        'ą':'a',
        'ć':'c',
        'ę':'e',
        'ł':'l',
        'ń':'n',
        'ó':'o',
        'ś':'s',
        'ź':'z',
        'ż':'z'
    }    
    return "".join([polish.get(char, char) for char in st])

