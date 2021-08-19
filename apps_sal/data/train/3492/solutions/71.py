def correct_polish_letters(st):
    polish_letters = 'ąćęłńóśźż'
    english_letters = 'acelnoszz'
    table = st.maketrans(polish_letters, english_letters)
    return st.translate(table)
