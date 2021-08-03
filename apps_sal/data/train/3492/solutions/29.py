def correct_polish_letters(st):
    change = str.maketrans('ąćęłńóśźżz', 'acelnoszzz')
    return st.translate(change)
