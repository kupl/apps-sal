def correct_polish_letters(st): 
    alp = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
    for key in alp.keys():
        st = st.replace(key, alp[key])
    return st
