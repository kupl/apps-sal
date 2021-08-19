X = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}


def correct_polish_letters(st):
    for x in X:
        st = st.replace(x, X[x])
    return st
