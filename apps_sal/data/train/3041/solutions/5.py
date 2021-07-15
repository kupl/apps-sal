def vowel_start(st): 
    return ''.join(' ' * (i in 'aeiou') + i for i in st.lower() if i.isalnum()).strip()
