def correct_polish_letters(st):
    polish = 'ąćęłńóśźż'
    english = 'acelnoszz'
    for i in range(9):
        st = st.replace(polish[i], english[i])
    return st
