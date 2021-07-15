def vowel_start(st): 
    return ''.join(f'{" " * (c in "aeiou")}{c}' for c in st.lower() if c.isalnum()).lstrip()
