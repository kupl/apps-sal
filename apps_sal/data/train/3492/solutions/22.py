def correct_polish_letters(st):
    map = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
    for key in map.keys():
        st = st.replace(key, map[key])
    return st
