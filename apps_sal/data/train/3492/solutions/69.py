import re
polist_letters = {
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

def correct_polish_letters(st): 
    my_st = st
    for l in polist_letters:
        my_st = re.sub(l, polist_letters.get(l), my_st)
    return my_st

