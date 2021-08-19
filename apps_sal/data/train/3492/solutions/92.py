def correct_polish_letters(st):
    translationTable = str.maketrans('ąćęłńóśźż', 'acelnoszz')
    return st.translate(translationTable)
