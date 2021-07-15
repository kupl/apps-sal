def correct_polish_letters(st): 

    if 'ą' in st:
        st = st.replace('ą','a')
    if 'ć' in st:
        st = st.replace('ć','c')
    if 'ę' in st:
        st = st.replace('ę','e')
    if 'ł' in st:
        st = st.replace('ł','l')
    if 'ń' in st:
        st = st.replace('ń','n')
    if 'ó' in st:
        st = st.replace('ó','o')
    if 'ś' in st:
        st = st.replace('ś','s')
    if 'ź' in st:
        st = st.replace('ź','z')
    if 'ż' in st:
        st = st.replace('ż','z')
        
    return st
        

