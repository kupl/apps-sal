def correct_polish_letters(st): 
    pol = {'ą': 'a',
           'ć': 'c',
           'ę': 'e',
           'ł': 'l',
           'ń': 'n',
           'ó': 'o',
           'ś': 's',
           'ź': 'z',
           'ż': 'z'}
    
    st2 = ""
    
    for c in st:
        if c in pol:
            st2 += pol[c]
        
        else:
            st2 += c
    
    return st2
