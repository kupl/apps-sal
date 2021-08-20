def correct_polish_letters(st):
    letters = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
    for l in st:
        if l in letters:
            st = st.replace(l, letters[l])
    return st
