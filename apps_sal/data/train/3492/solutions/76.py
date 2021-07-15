def correct_polish_letters(st): 
    dict = {
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
    for key in dict.keys():
        st = st.replace(key, str(dict[key]))
            
    return st
