def correct_polish_letters(st):
    dic = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
    for i in dic:
        st = st.replace(i, dic[i])
    return st
