intab = 'ąćęłńóśźż'
outtab = 'acelnoszz'
polish = str.maketrans(intab, outtab)


def correct_polish_letters(st):
    return st.translate(polish)
