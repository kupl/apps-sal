def correct_polish_letters(st):
    # your code here
    polish = {
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

    res = ''
    for i in st:
        if i in polish:
            q = st.index(i)
            res += st[q].replace(st[q], polish.get(st[q]))
        else:
            res += i

    return res
