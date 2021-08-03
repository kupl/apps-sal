def correct_polish_letters(st):
    table = st.maketrans("ąćęłńóśźż", "acelnoszz")
    st = st.translate(table)
    return st
