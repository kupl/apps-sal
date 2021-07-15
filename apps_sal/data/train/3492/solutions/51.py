def correct_polish_letters(st):
    d = {
        'ą': 'a', 'ć': 'c', 'ę': 'e',
        'ł': 'l', 'ń': 'n', 'ó': 'o',
        'ś': 's', 'ź': 'z', 'ż': 'z'
    }
    for k in d:
        st = st.replace(k, d[k])
    return st
