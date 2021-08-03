pol = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
       'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}


def correct_polish_letters(st):
    for char in st:
        if char in pol.keys():
            st = st.replace(char, pol.get(char))
    return st
