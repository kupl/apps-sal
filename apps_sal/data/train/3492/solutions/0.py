def correct_polish_letters(s):
    return s.translate(str.maketrans("ąćęłńóśźż", "acelnoszz"))
