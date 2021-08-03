def correct_polish_letters(st):
    char = ['a', 'c', 'e', 'l', 'n', 'o', 's', 'z', 'z']
    mod = ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż']
    for x in st:
        if x in mod:
            st = st.replace(x, char[mod.index(x)])
    return st
