def correct_polish_letters(st): 
    for p,e in {"ą":"a","ć":"c","ę":"e","ł":"l","ń":"n","ó":"o","ś":"s","ź":"z","ż":"z"}.items():
        st=st.replace(p,e)
    return st
