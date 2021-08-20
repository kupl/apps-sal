dic = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}


def correct_polish_letters(st):
    for (key, val) in list(dic.items()):
        if key in st:
            st = st.replace(key, val)
    return st
