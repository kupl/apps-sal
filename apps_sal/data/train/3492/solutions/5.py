def correct_polish_letters(stg): 
    return stg.translate(str.maketrans("ąćęłńóśźż", "acelnoszz"))
