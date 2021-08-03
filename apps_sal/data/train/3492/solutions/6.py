def correct_polish_letters(st):
    return st.translate(st.maketrans("ąćęłńóśźż", "acelnoszz"))
