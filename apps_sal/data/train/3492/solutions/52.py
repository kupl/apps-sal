def correct_polish_letters(st):
    alp = "ąćęłńóśźż"
    alpc = "acelnoszz"
    return st.translate(st.maketrans(alp, alpc))
