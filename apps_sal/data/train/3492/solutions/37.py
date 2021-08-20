def correct_polish_letters(st):
    (polish, latin) = ('ąćęłńóśźż', 'acelnoszz')
    for i in polish:
        st = st.replace(i, latin[polish.find(i)])
    return st
