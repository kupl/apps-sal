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
    for c in st:
        if c in dict:
            st = st.replace(c, dict[c])
    return st
